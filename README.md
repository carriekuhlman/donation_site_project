## Donation Helper
Donation Helper was designed to give non-profit organizations a way to show potential donors which items they need through a searchable database.  Donors can search for an item and the results table displays item name, organization, location, condition accepted, and quantity needed. Bootstrap modals help provide additional location and organization details without requiring a page reload. Organization accounts have the ability to add both new locations and items to the database. Future plans for the app include adding geolocation functionality with an API, add the ability to create a donated goods list to improve donor experience, and allow organizations to update item quantities as donations come in.

## About the Developer
Carrie Kuhlman is a film school graduate turned tech enthusiast. In 2012, she started working as an admin assistant at a tech company. She quickly found that she loved solving tech problems much more than answering the phones. She has managed and executed a whole host of projects including on-premise Exchange to hosted Office 365 migrations, full  infrastructure upgrades, and full site moves for her clients. She is also the go-to family member for "when the Apple TV is doing that thing again." Carrie is currently the Director of Operations for an IT Managed Service Provider in Los Angeles. She constantly found herself digging deep into logs to solve problems and wanted to explore software engineering to get a better understanding of how things work. In the next few years, she intends to focus on improving efficiencies and operations at her current company; leveraging and expanding on the skills that she has gained. Carrie plans on building out a development/engineering department, focusing on improving diversity and inclusion. The long-term dream is to be working in Robotics, helping to engineer either the latest animatronic at Disneyland or a flashy new Mars rover for NASA.

## Technologies
* Python
* Flask
* Jinja2
* PostgreSQL
* SQLAlchemy
* JavaScript
* jQuery
* HTML
* CSS
* Bootstrap

## Features

#### Database

The app is built on a PostgreSQL database using 5 tables: Users, Donors, Orgs, Locations, and Items. Each registered account will have a record in the Users table, and either a record in the Donors or Orgs table. The user_id exists as a foreign key in both 

![alt text](https://github.com/carriekuhlman/donation_site_project/blob/main/static/img/data_model.png "Donation Helper Data Model")

#### Homepage

From the homepage users can login, create an account, or search the database for needed items. The radio buttons on the create account form utilize an event listener and execute an AJAX request to upon click to adjust the form fields based on selection. 

If a user attempts to login to an account that does not exist, and Flask flash message will be generated and the user will be redirected to a create account page. 
Once a user successfully creates either a donor or organization account, they will be prompted to log in to get to the user account the page. 

The nav bar also allows for login, account access, item search and logging out.

![alt text](https://github.com/carriekuhlman/donation_site_project/blob/main/static/img/homepage.png "Donation Helper Homepage")

#### User Account Page

The user account page displays different content depending on account type. The logged in user's session is tracked and a function within a Flask route handles the rendering of the appropriate HTML page. In the future, this will be handled on the client side using React. 

The donor user account page currently includes the functionality to search the needed items list. After searching an item, the search results page is displayed. Bootstrap modals allows the user to get more details on the item's organization and location without leaving the search results page. 

The organization account page includes the ability to add items and new locations. The "Add Item" Boostrap form includes a drop-down menu that displays all items for the logged-in organization. The appearance of the locations in a drop-down menu was accomplished using a Jinja for loop, passing in a list of location objects retrieved through a function which returns the results of a SQLAlchemy query.

## Future Features

* Google Maps or Geocodio API integration to search for items by geolocation
* Functionality for donor accounts to add items to their "to-do" list
* Ability for org accounts to adjust item quantities needed and move items to different locations
* Ability for org accounts to create an emailable/texatble/printable item receipt for donors in a few simple clicks

The goal is to make Donation Helper a one-stop-shop for both non-profits and organizations to easily exchange goods. This will hopefully minimize waste and get donated goods into the hands of the small non-profits that need them.

## Installation
To run Donation Helper on your own machine:

Install PostgreSQL

Clone or fork this repo:
```
https://github.com/carriekuhlman/donation_site_project
```
Create and activate a virtual environment inside your Donation Helper directory:
```
virtualenv env
source env/bin/activate
```

Install the dependencies:
```
pip3 install -r requirements.txt
```
Set up the database with table structure only:

```
createdb donations
python3 -i model.py
db.create_all()
```

OR set up the database and seed the database with dummy data (optional):

```
python3 seed_database.py
```

Run the app:

```
python3 server.py
```

You can now navigate to 'localhost:5000/' to access Donation Helper.
