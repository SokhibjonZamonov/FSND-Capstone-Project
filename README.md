

# Full Stack Capstone Project

## Casting Agency App
This is my final project for Udacity Full Stack Developer course. I decided to work on a suggested
topic (Casting agency) for this last project, even though it was voluntary. I created a website where movie makers can see, add, delete, patch, and post actors or movies.
The database tables store basic data about actors and movies.

The project is currently deployed in Heroku: [https://fatidique-mandarine-59515.herokuapp.com/](https://fatidique-mandarine-59515.herokuapp.com/)

## Getting started

### Installing Dependencies
**Python 3.8.2**

The dependencies for the project can be installed with pip:
  > pip install -r requirements.txt

#### Key Dependencies
- [Flask](http://flask.pocoo.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Deployment
To deploy the code in heroku, follow the below instructions:

### Install Heroku CLI

[https://devcenter.heroku.com/categories/command-line](https://devcenter.heroku.com/categories/command-line)

### Log in with command line
> heroku login

### Save package requirements
> pip freeze > requirements.txt

 ### Environment Configuration
 Use 
 > touch setup.sh

and set up all of your environment variables in that file.
### Gunicorn
First, we need to install gunicorn using `pip install gunicorn`. Next `touch Procfile` to create the file.
It (Procfile) only needs to include one line to instruct Heroku correctly for us: `web: gunicorn app:app`.

### Database Manage & Migrations on Heroku
Heroku can run all your migrations to the database you have hosted on the platform, but in order to do so, your application needs to include a  `manage.py`  file.

We'll need three new packages in the file. Run the following commands to install them:

```
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
```

The  `manage.py`  file will contain the following code:

```
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

```

Now we can run our local migrations using our  `manage.py`  file, to mirror how Heroku will run behind the scenes for us when we deploy our application:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
you installed new packages you need to use freeze again to update the `requirements.txt` file

## Deploying to Heroku
Create the Heroku app running 

`heroku create name_of_your_app`.

**Note**: *If you don't specify your app name, Heroku names it with random words*

### Deploy your code

`cd`  to your project repository and run:

    git init
    git add .
    git commit -m 'first commit'
    git push heroku master
    git remote add heroku heroku_git_url

#### Add postgresql add on for our database
Run this code in order to create your database and connect it to your application: 
`heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application`

Run 
`heroku config --app name_of_your_application` 
in order to check your configuration variables in Heroku.

#### Fix configurations in Heroku
Go to your Heroku Dashboard and access your application's settings. Reveal your config variables and start adding all the required environment variables for your project.

#### Push it!
Push it up!  `git push heroku master`

#### Run migrations

Once your app is deployed, run migrations by running:  `heroku run python manage.py db upgrade --app name_of_your_application`

# And now you have a live application! 😊

## API Documentation

-   To see API endpoints navigate to [API Endpoints]()

### Role Based Access

-   Public endpoint - No authorization is required
- Casting Assistant - Can view actors and movies
- Casting Director -  All permissions a Casting Assistant has and can add or delete an actor from the database. As well as modify actors or movies
- Executive Producer - All permissions a Casting Director has and can add or delete a movie from the database

### Error Handlers

API returns the following errors in the JSON format:

-   400: Bad request
-   401: Unauthorized
-   403: Forbidden
-   404: Page not found
-   500: Internal Server Error

```
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```
### Testing
To run tests with RBAC, import [collection](https://github.com/SokhibjonZamonov/FSND-Capstone-Project/blob/master/API_README.md) in [Postman](https://www.postman.com/)