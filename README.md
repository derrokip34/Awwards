# AWWARDS

## AUTHOR
- [Derrick Kiprop](https://github.com/derrokip34)

## PROJECT DESCRIPTION
This django app allows user to post their projects for review and rating.The user can also review and rate other projects from different users

## SETUP AND USAGE INSTRUCTIONS
### Prerequisites
- A web browser
- Github account
- Terminal
- Python3.6
- Text editor software

#### Clone or download the zip file of this repository
- Clone by typing in the following command `git clone https://github.com/derrokip34/Awwards.git`
- If you've downloaded the zip extract it in your preferred destination

#### Navigate into the project directory

#### Install python3.6 if not yet installed

##### Install virtual environment by typing the following command
`python3.6 -m venv --without-pip virtual`

#### Activate virtual environment
`source virtual/bin/activate`

#### Install pip
`curl https://bootstrap.pypa.io/get-pip.py | python`

#### Install dependencies by typing the following command
`pip install -r requirements.txt`

#### Create an `.env` file and edit it where appropriate
```bash
SECRET_KEY = <your secret key>
DB_NAME = <your database name>
DB_USER = <your database username>
DB_PASSWORD = <your database password>
DEBUG= <True or False>
MODE= <mode>
PORT= '5432'
DB_HOST = '127.0.0.1'
```
#### Run the following commands in your terminal
```bash
source .env
python3.6 manage.py runserver
```

#### Open 'http://127.0.0.1:8000/' in your browser and enjoy your app

## [Awwards Live site](https://my-awwards.herokuapp.com/)

## BDD
### Input required
- Registration details or login details
- Project and project's details
- New user details when updating user profile

### Behaviour
- The app will save user's details upon registration
- If a user is logging in it will confirm the details inputted
- Project and its details will be saved

### Output
- The user will be directed to the homepage where they will see projects posted by other users
- User's profile page will display user's projects and their information

## TECHNOLOGIES USED
- HTML
- CSS
- Bootstrap 4
- Material Design Bootstrap
- Python3.6
- Django
- Markdown
- Heroku
- PostgreSQL

## BUGS
There are no known bugs at the moment
In case of any bugs contact me at derrickip34@gmail.com

## LICENSE & COPYRIGHT INFORMATION
[MIT License](https://github.com/derrokip34/Awwards/blob/master/license.md)
