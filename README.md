# Warbler

## About

Warbler is a Flask-backed web that is inspired by Twitter deployed with Heroku.

Features include:
- Register and Login
- Follow other users
- Post a message
- Like or Unlike other users' messages
- Edit profile image, personal bio, and background header

## [Live Demo](https://edwinkim-demo-jobly.surge.sh/)

# Getting Started on the Development Server

### In your terminal run these commands:

1. clone the repo
2. `cd flask-warbler`
3. Make sure you are in a virtual environment
4. `pip install -r requirements.txt`
5. `psql`
6. `CREATE DATABASE warbler`
7. `CREATE DATABASE warbler_test`
7. Exit psql
8. `python seed.py` (seeds database with sample users and messages)

#### Create a .env file in the root directory and create these variables (choose your own secret key)
- SECRET_KEY=
- DATABASE_URL=postgresql:///warbler

#### Start the server

1. `flask run`

- Runs the app in the development mode.
- You can view app in browser at [http://localhost:5000](http://localhost:5000).

### Testing the app
#### To test the entire app:

1. `python3 -m unittest`

#### To test a specific folder:

1. `python3 -m unittest {name_of_test_file}`
