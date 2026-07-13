## Issue and Vulnerability Tracking System ##

## project Description
This project is a RESTful API developed using Flask and Flask-SQLAlchemy.It allows users to manage software issues and security vulnerabilities through CRUD operation, search and filtering ,and reporting features.The application stores data in a SQLite database.


## Features
-Create,view , update, and delete issues
-Create,view,update and delete vulnerabilities
-Search issues by status
-Search issues by priority
-Search vulnerabilitieis by severity
-Generate summary reports
-Store data using a SQLite database
-Test API endpoints using

## Technoligies used
-Python 3.14
-Flask
-Flask-SQLAlchemy
-SQLite
-Git
-GitHub
-Postman
-Visual Studion Code

## Installation

1. Clone the repository:


git clone https://github.com/Milan9158/Advanced_Programming_Techniques_CA2.git


2. Navigate to the project folder:


cd Advanced_Programming_Techniques_CA2


3. Create a virtual environment:


py -3.14 -m venv venv


4. Activate the virtual environment (Windows PowerShell):


.\venv\Scripts\Activate.ps1


5. Install the required packages:

pip install -r requirements.txt


6. Run the application:


python app.py


The application will be available at:


http://127.0.0.1:5000



## API Endpoints

### Home
- GET /

### Issues
- GET /issues
- POST /issues
- PUT /issues/<id>
- DELETE /issues/<id>

### Search Issues
- GET /issues/status/<status>
- GET /issues/priority/<priority>

### Vulnerabilities
- GET /vulnerabilities
- POST /vulnerabilities
- PUT /vulnerabilities/<id>
- DELETE /vulnerabilities/<id>

### Search Vulnerabilities
- GET /vulnerabilities/severity/<severity>

### Reports
- GET /reports/issues
- GET /reports/vulnerabilities


##  References

This project was developed independently and adapted from the following official documentation:

- Flask Documentation: https://flask.palletsprojects.com/
- Flask-SQLAlchemy Documentation: https://flask-sqlalchemy.palletsprojects.com/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- Python Documentation: https://docs.python.org/3/

## Author

**Milan**

Advanced Programming Techniques CA2