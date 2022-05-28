## Cloud Sound Gallery App
This is my first Django Independent Project

## SCREENSHOT
![image](https://user-images.githubusercontent.com/85553801/170823580-d7dc4396-29bb-473d-8c4f-789ab65e6267.png)

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
 
 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 
 ## ACKNOWLEDGEMENTS
 I acknowledge Maryann Mwikali as my technical mentor while learning Django
