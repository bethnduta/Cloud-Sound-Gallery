## Cloud Sound Gallery App
This is my first Django Independent Project

## Description
Cloud Sound is a photo web application that showcase beautiful photos in different categories.
As a user you can:
* view different photos that interest you
* Click on a single photo to expand it and also view the details of the photo.
* Search for different categories of photos
* copy a link to the photo to share with your friends
* view photos based on the location they were taken

## TECHNOLOGIES USED
* Python3.9
* Django MVC framework
* HTML, CSS, BOOTSTRAP
* Javascript
* Postgresql
* Heroku

## SETUP/INSTALLATION REQUIREMENTS
To access the code:
* clone the repo https://github.com/bethnduta/Cloud-Sound-Gallery.git
### activate virtual environment
Activate virtual environment using python3.9 as default handler virtualenv env && env\Scripts\activate
### Install dependencies
Install dependencies that will create an environment for the app to run pip install -r requirements.txt
### Create the database
-- psql
- CREATE DATABASE gallery;

### .env file
CReate .env file and paste the following filling where necessary:
SECRET_KEY = <'secret_key>'
DBNAME = 'gallery'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
### Run initial migration
python3.9 manage.py runmigrations gallery
python3.9 manage.py migrate
#### Run the app
python3.9 manage.py runserver
Open terminal on localhost:8000

## Current Bugs
There are no known bugs as of now. Incase you find one feel free to solve the bug and push the changes.

## SUPPORT AND CONTACT DETAILS
incase you want to contribute to the project fork the repository and make changes. Incase you wish to brainstorm any idea concerning the project kindly keep in touch with me through my 
* email [bethnduta05@gmail.com]
* slack bethnduta

## LICENSE
MIT Copyright (c) 2022