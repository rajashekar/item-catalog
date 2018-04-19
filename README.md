# item-catalog
This project is done as part of Udacity Fullstack Developer course. The purpose of the project is to understand the concepts Python framework Flask along with implementing third-party OAuth authentication and to develop a RESTful web application to display categories and items and gives logined user to edit or add items. 
## Getting Started
### Prerequesites
Below software needs to be installed
 - [Python](https://www.python.org/downloads/) 
 - [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
 - [Vagrant](https://www.vagrantup.com/downloads.html)

 ### Installing
To download the virtual machine using vagrant file
```
git clone https://github.com/udacity/fullstack-nanodegree-vm.git
```
To install downloaded virtual machine 
```
cd fullstack-nanodegree-vm
vagrant up
```
To login to vagrant virtual machine
```
vagrant ssh
```
### How to Run
```
git clone https://github.com/rajashekar/item-catalog.git
cd item-catalog
python catalog_views.py
```
open http://localhost:5000/

![Demo](demo.png?raw=true "Demo")

### Available json endpoints
http://localhost:5000/catalog.json
```
{
  "categories": [
    {
      "id": 1, 
      "items": [
        {
          "category": "TV", 
          "description": "Samsung TV 55 inch 4K", 
          "id": 1, 
          "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
          "title": "Samsung TV", 
          "user_id": 1
        }, 
        {
          "category": "TV", 
          "description": "LG TV 55 inch 4K", 
          "id": 2, 
          "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
          "title": "LG TV", 
          "user_id": 1
        }
      ], 
      "name": "TV"
    }, 
    {
      "id": 2, 
      "items": [
        {
          "category": "Gaming Console", 
          "description": "Console game by Sony", 
          "id": 3, 
          "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
          "title": "Sony playstation 4", 
          "user_id": 1
        }, 
        {
          "category": "Gaming Console", 
          "description": "Console game by Microsoft", 
          "id": 4, 
          "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
          "title": "Xbox one", 
          "user_id": 1
        }, 
        {
          "category": "Gaming Console", 
          "description": "Console game by Nintendo", 
          "id": 5, 
          "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
          "title": "Nintendo", 
          "user_id": 1
        }
      ], 
      "name": "Gaming Console"
    }
  ]
}
```
http://localhost:5000/items.json
```
{
  "items": [
    {
      "category": "TV", 
      "description": "Samsung TV 55 inch 4K", 
      "id": 1, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "Samsung TV", 
      "user_id": 1
    }, 
    {
      "category": "TV", 
      "description": "LG TV 55 inch 4K", 
      "id": 2, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "LG TV", 
      "user_id": 1
    }, 
    {
      "category": "Gaming Console", 
      "description": "Console game by Sony", 
      "id": 3, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "Sony playstation 4", 
      "user_id": 1
    }, 
    {
      "category": "Gaming Console", 
      "description": "Console game by Microsoft", 
      "id": 4, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "Xbox one", 
      "user_id": 1
    }, 
    {
      "category": "Gaming Console", 
      "description": "Console game by Nintendo", 
      "id": 5, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "Nintendo", 
      "user_id": 1
    }
  ]
}
```
http://localhost:5000/catalog/\<category>/items/json

Example - 
http://localhost:5000/catalog/TV/items/json
```
{
  "items": [
    {
      "category": "TV", 
      "description": "Samsung TV 55 inch 4K", 
      "id": 1, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "Samsung TV", 
      "user_id": 1
    }, 
    {
      "category": "TV", 
      "description": "LG TV 55 inch 4K", 
      "id": 2, 
      "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
      "title": "LG TV", 
      "user_id": 1
    }
  ]
}
```
http://localhost:5000/catalog/\<category>/\<item>/json

http://localhost:5000/catalog/TV/LG%20TV/json
```
{
  "item": {
    "category": "TV", 
    "description": "LG TV 55 inch 4K", 
    "id": 2, 
    "modified_date": "Sun, 15 Apr 2018 06:40:28 GMT", 
    "title": "LG TV", 
    "user_id": 1
  }
}
```