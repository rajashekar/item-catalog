from flask import Flask, request, render_template, make_response, flash, redirect, jsonify
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

import httplib2
import random
import string
import json
import requests

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(open('client_secret_google.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog App"    

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def showMain():
    categories = session.query(Category).order_by(asc(Category.name))
    items =  session.query(Item).order_by(asc(Item.modified_date))
    return render_template('catalog.html', categories=categories, items=items, page="list")

@app.route('/catalog/<string:cat_name>/items')
def showCategory(cat_name):
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).filter_by(category_name = cat_name).all()
    return render_template('catalog.html', categories=categories, 
            items=items, cat_name=cat_name, page="category", size=len(items))

@app.route('/catalog/<string:cat_name>/<string:item_name>')
def showItem(cat_name, item_name):
    item = session.query(Item).filter_by(category_name = cat_name, title = item_name).one()
    return render_template('item.html', item=item)

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state, session=login_session)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # if token is not valid, return error
    print "request args :", request.args
    print "login session ",login_session
    if request.args.get('state') != login_session['state']:
        return sendreponse('Invalid state parameter.',401)
    # get the code
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secret_google.json',scope='')
        print "here 1"
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        return sendreponse('Failed to upgrade the authorization code.',401)

    # check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http() 
    result = json.loads(h.request(url, 'GET')[1]) 
    if result.get('error') is not None:
        return sendreponse(result.get('error'),500)

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']     
    if result['user_id'] != gplus_id:
        return sendreponse("Token's user ID does'nt match given user ID.",401)

    #Verify that the access token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        return sendreponse("Token's client ID does'nt match.",401)

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['username'] = data['name']  
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/disconnect')
def disconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Acess Token is None'
        return sendreponse('Current user not connected', 401)
    print 'In disconnect access token is %s', access_token
    print 'User name is: ', login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is', result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        print 'Successfully disconnected'
        return redirect('/')
    else: 
        return sendreponse('Failed to revoke token for given user.',400)    

def sendreponse(message, statusCode):
    response = make_response(json.dumps(message),statusCode)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/catalog.json')
def catalogJSON():
    categories = session.query(Category).all()
    response = []
    for cat in categories:
        items = session.query(Item).filter_by(category_name = cat.name).all()
        res = cat.serialize
        res['items'] = [r.serialize for r in items]
        response.append(res)
    return jsonify(categories=[r for r in response])

@app.route('/items.json')
def itemsJSON():
    items = session.query(Item).all()
    return jsonify(items=[r.serialize for r in items])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
