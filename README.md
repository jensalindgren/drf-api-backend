# Gymhub API

## Project Goals

This project provides a Django Rest Framework API for a gym network. It has also a React frontend to interact with the API.

Gymhub is a platform that allows it gym members to post comment and get information about the gym they are subscribed to. It also allows the gym owners to manage their gym and their members trough the platform.

## Table of Contents
- [Gymhub API](#gymhub-api)
  - [Project Goals](#project-goals)
  - [Table of Contents](#table-of-contents)
  - [Planning](#planning)
  - [Database Structure](#database-structure)
  - [Models](#models)
    - [Profile](#profile)
    - [Post](#post)
    - [Comment](#comment)
    - [Likes](#likes)
    - [Followers](#followers)
    - [Upvotes](#upvotes)
    - [Events](#events)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [PEP8 Validation](#pep8-validation)
    - [PEP8 Validation Results](#pep8-validation-results)
    - [drf\_api\_backend PEP8 Validation Results](#drf_api_backend-pep8-validation-results)
    - [Posts PEP8 Validation Results](#posts-pep8-validation-results)
    - [Profiles PEP8 Validation Results](#profiles-pep8-validation-results)
    - [Comments PEP8 Validation Results](#comments-pep8-validation-results)
    - [Likes PEP8 Validation Results](#likes-pep8-validation-results)
    - [Upvotes PEP8 Validation Results](#upvotes-pep8-validation-results)
    - [Events PEP8 Validation Results](#events-pep8-validation-results)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Packages](#packages)
    - [Tools](#tools)
  - [Deployment](#deployment)
    - [1. Create a a database in ElephantSQL](#1-create-a-a-database-in-elephantsql)
    - [2. Create a new app in Heroku](#2-create-a-new-app-in-heroku)
    - [3. Set up the environment variables](#3-set-up-the-environment-variables)
    - [4 Confirming your app is connected to your external database](#4-confirming-your-app-is-connected-to-your-external-database)
    - [5. Preparing for deployment](#5-preparing-for-deployment)
    - [6. Deploying to Heroku](#6-deploying-to-heroku)
    - [Done - Congratulations!](#done---congratulations)
  - [Credits](#credits)
    - [Acknowledgements](#acknowledgements)

## Planning

Planning was done with user stories for the here for the backend. I started to lay up the most important models and their relationships. I also started to think about the endpoints and the serializers. I also started to think about the frontend and the components I would need.

## Database Structure

## Models

Data model was planned in parallel with the user stories and API endpoints.
Database models are defined in the models.py file. The models are:

### Profile

It represents the user profile, using one to one relationship to a user model. A profile can be a gym owner or a gym member. It automatically creates a profile when a user is created.

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE                                |
| created_at                   | DateTimeField | auto_now_add=True                                             |
| updated_at                   | DateTimeField | auto_now=True                                                 |
| is_staff                     | BooleanField  | default=False                                                 |
| first_name                   | CharField     | max_length=255, blank=True                                    |
| last_name                    | CharField     | max_length=255, blank=True                                    |
| content                      | TextField     | blank=True                                                    |
| profile_image                | ImageField    | upload_to='images/', default='../default_profile_j1uwjo'      |

### Post

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| title                        | CharField     | max_length=255                                                |
| content                      | TextField     | blank=True                                                    |
| created_at                   | DateTimeField | auto_now_add=True                                             |
| updated_at                   | DateTimeField | auto_now=True                                                 |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE,related_name="posts"           |
| profile_image                | ImageField    | upload_to='images/', default='../default_post_sqpxy8',        |

### Comment

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE                                |
| post                         | ForeignKey    | Post, on_delete=models.CASCADE                                |
| created_at                   | DateTimeField | auto_now_add=True                                             |
| updated_at                   | DateTimeField | auto_now=True                                                 |
| content                      | TextField     | blank=True                                                    |

### Likes

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE                                |
| post                         | ForeignKey    | Post, related_name='likes', on_delete=models.CASCADE          |
| created_at                   | DateTimeField | auto_now_add=True                                             |

### Followers

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| owner                        | ForeignKey    | User, related_name='following', on_delete=models.CASCADE      |
| followed                     | ForeignKey    | User, related_name='followed', on_delete=models.CASCADE       |
| created_at                   | DateTimeField | auto_now_add=True                                             |

### Upvotes

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| title                        | ForeignKey    | User, on_delete=models.CASCADE                                |
| post                         | ForeignKey    | Post, on_delete=models.CASCADE,related_name='upvotes'         |
| created_at                   | DateTimeField | auto_now_add=True                                             |

### Events

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| title                        | CharField     | max_length=100                                                |
| content                      | TextField     | blank=True                                                    |
| created_at                   | DateTimeField | auto_now_add=True                                             |
| updated_at                   | DateTimeField | auto_now=True                                                 |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE,related_name='events'          |
| content                      | TextField     | blank=True                                                    |
| image                        | ImageField    | upload_to="images/", default='../default_post_sqpxy8'         |

## Testing

### Manual Testing

| Application | Endpoint                  | Expected Result                                                                                                                                              | Pass/Fail |
| ----------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------| --------- |
| Profiles    | profiles/                 | Returns a list of all the profiles in the database ordered by creation date                                                                                  | Pass      |
| Profiles    | profiles/                 | Applying all the right filter for the profiles                                                                                                               | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user isn't the owner of the profile, they can't edit or delete it        | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user is the owner of the profile, they can edit and delete it            | Pass      |
| Comments    | comments/                 | Return a list of all the comments in order of creation date                                                                                                  | Pass      |
| Comments    | comments/                 | Applying all the right filter for the comments                                                                                                               | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values                                                                                     | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and the owner can edit and delete the comment                                       | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and if the user isn't the owner of the comment, they can't edit or delete i         | Pass      |
| Posts       | posts/                    | Return a list of all the posts in order of creation date                                                                                                     | Pass      |
| Posts       | posts/                    | Applying all the right filter for the posts                                                                                                                  | Pass      |
| Posts       | posts/<int:pk>/           | Returns a single post with a correct ID and a list of all it's values and the owner can edit and delete the post                                             | Pass      |
| Posts       | posts/<int:pk>/           | Returns a single posts with a correct ID and a list of all it's values and if the user isn't the owner of the posts, they can't edit or delete i             | Pass      |
| Posts       | posts/<int:pk>/           | Returns a single posts with a correct ID and a list of all it's values and even if the user is a staff member, they can't edit and delete it                 | Pass      |
| Followers   | followers/                | Return a list of all the profiles and its followers                                                                                                          | Pass      |
| Followers   | followers/<int:pk>/       | Return a single ID of profile and all its value you can choose to follow user. And unfollow                                                                  | Pass      |
| Followers   | followers/<int:pk>/       | Return a single ID of profile and all its value you can choose to follow user. And unfollow, if the user isn't the owner of the profile, they can't unfollow | Pass      |
| Likes       | likes/                    | Return a list of all the likes for posts                                                                                                                     | Pass      |
| Likes       | likes/<int:pk>/           | Returns a single like with correct ID and list of all its value, owner of the like can delete the like                                                       | Pass      |
| Likes       | likes/<int:pk>/           | Returns a single like with correct ID and list of all its value, if the user isn't the owner of the like, they can't delete it                               | Pass      |
| Events      | events/                   | Return a list of all the posts in order of creation date                                                                                                     | Pass      |
| Events      | events/                   | Applying all the right filter for the events                                                                                                                 | Pass      |
| Events      | events/<int:pk>/          | Returns a single event with a correct ID and a list of all it's values and the owner can edit and delete the event                                           | Pass      |
| Events      | events/<int:pk>/          | Returns a single event with a correct ID and a list of all it's values and if the user isn't the owner of the event, they can't edit or delete i             | Pass      |
| Upvotes     | upvotes/                  | Returns a list of all the current upvotes in the database                                                                                                    | Pass      |
| Upvotes     | upvotes/                  | If a user is logged out they are not able to upvote a post                                                                                                   | Pass      |
| Upvotes     | upvotes/<int:pk>/         | Returns a single upvote with a correct ID and a list of all it's values                                                                                      | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote, they are unable to delete the upvote                                                                             | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote but is a staff member, they are unable to delete the upvote                                                       | Pass      |

## PEP8 Validation

PEP8 online was used to validate the python code in the application.

### PEP8 Validation Results

| File Name                    | Result |
| ---------------------------- | ------ |
| `__init__.py`                | Pass   |
| `admin.py`                   | Pass   |
| `apps.py`                    | Pass   |
| `models.py`                  | Pass   |
| `serializers.py`             | Pass   |
| `tests.py`                   | Pass   |
| `urls.py`                    | Pass   |
| `views.py`                   | Pass   |
| `settings.py`                | Pass   |
| `wsgi.py`                    | Pass   |
| `manage.py`                  | Pass   |

Here is a screenshot of the apps results:

### drf_api_backend PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_%20(3).png)
![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_%20(4).png)
![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_%20(5).png)
![PEP8 Validation Results](/documentation/readme_images/drf_api_backend/pep8ci.herokuapp.com_.png)

### Posts PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/posts/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/posts/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/posts/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/posts/pep8ci.herokuapp.com_%20(3).png)

### Profiles PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/profiles/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/profiles/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/profiles/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/profiles/pep8ci.herokuapp.com_%20(3).png)

### Comments PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/comments/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/comments/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/comments/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/comments/pep8ci.herokuapp.com_%20(3).png)

### Likes PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/likes/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/likes/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/likes/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/likes/pep8ci.herokuapp.com_%20(3).png)

### Upvotes PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/upvotes/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/upvotes/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/upvotes/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/upvotes/pep8ci.herokuapp.com_%20(3).png)

### Events PEP8 Validation Results

![PEP8 Validation Results](/documentation/readme_images/events/pep8ci.herokuapp.com_.png)
![PEP8 Validation Results](/documentation/readme_images/events/pep8ci.herokuapp.com_%20(1).png)
![PEP8 Validation Results](/documentation/readme_images/events/pep8ci.herokuapp.com_%20(2).png)
![PEP8 Validation Results](/documentation/readme_images/events/pep8ci.herokuapp.com_%20(3).png)

I find that the PEP8 validation results are very useful as they help me to write clean code and to follow the best practices of writing code in Python.
Did not have any issues with the PEP8 validation results.

[Back to top](#table-of-contents)

## Technologies Used

### Languages

Python a high level programming language was used to create the backend of the application.

### Libraries

Django a python web framework was used to create the backend of the application.
Django Rest Framework was used to create the API endpoints for the application.

### Packages

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
- [black](https://pypi.org/project/black/) - Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting.
- [charset-normalizer](https://pypi.org/project/charset-normalizer/) - The Real First Universal Charset Detector. This library is the implementation of the WHATWG Encoding Standard written in Python.
- [click](https://pypi.org/project/click/) - Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.
- [cloudinary](https://pypi.org/project/cloudinary/) - Cloudinary is a cloud service that offers a solution to a web application's entire image management pipeline.
- [cryptography](https://pypi.org/project/cryptography/) - cryptography is a package which provides cryptographic recipes and primitives to Python developers.
- [dj-database-url](https://pypi.org/project/dj-database-url/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - dj-rest-auth is a package providing authentication and registration / account management for Django Rest Framework.
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Django storage for Cloudinary.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds CORS (Cross-Origin Resource Sharing) headers to responses. This allows in-browser requests to your Django application from.
- [django-extensions](https://pypi.org/project/django-extensions/) - This is a repository for collecting global custom management extensions for the Django Framework.
- [django-filter](https://pypi.org/project/django-filter/) - Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code.
- [django-rest-auth](https://pypi.org/project/django-rest-auth/) - django-rest-auth is a package providing authentication and registration / account management for Django Rest Framework.
- [djangorestframework](https://pypi.org/project/djangorestframework/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - A JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.
- [httpie](https://pypi.org/project/httpie/) - HTTPie (pronounced aitch-tee-tee-pie) is a command line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible.
- [multidict](https://pypi.org/project/multidict/) - multidict implementation.
- [oauthlib](https://pypi.org/project/oauthlib/) - OAuthlib is a generic utility which implements the logic of OAuth without assuming a specific HTTP request object or web framework.
- [pathspec](https://pypi.org/project/pathspec/) - Utility library for gitignore style pattern matching of file paths.
- [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - A Python library which allows you to encode and decode JSON Web Tokens (JWT).
- [PySocks](https://pypi.org/project/PySocks/) - A Python SOCKS client module. See
- [python3-openid](https://pypi.org/project/python3-openid/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application.
- [pytz](https://pypi.org/project/pytz/) - World timezone definitions, modern and historical.
- [requests](https://pypi.org/project/requests/) - Requests is an elegant and simple HTTP library for Python, built for human beings.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - This project provides first-class OAuth library support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser module for Python.
- [urllib3](https://pypi.org/project/urllib3/) - urllib3 is a powerful, sanity-friendly HTTP client for Python.
### Tools

- [VSCode](https://code.visualstudio.com/) - IDE used to develop the application.
- [GitHub](https://github.com/) - Used to host and deploy the website as well as manage the project.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files .
- [Git](https://git-scm.com/) - Version control
- [Heroku](https://www.heroku.com/) - Deployment
- [ElephantSQL](https://www.elephantsql.com/) - Provides a browser tool for SQL queries where you can create, read, update and delete data directly from your web browser.
- [CI PEP8 Linter](https://pep8ci.herokuapp.com/#) - Used to check the Python code for any linting issues

[Back to top](#table-of-contents)

## Deployment

### 1. Create a a database in ElephantSQL

- Create a new database in ElephantSQL
- Login to ElephantSQL
- Click on the create new instance button
- Select the free plan
- Give the database a name
- Select a region
- Click on Review and create instance
- In the URL section, click the copy icon to copy the database URL

### 2. Create a new app in Heroku

- Login to Heroku
- Click on the new button
- Name the app
- Select the region closest to you
- Add a Config Var DATABASE_URL, and for the value, copy in your database URL from ElephantSQL

### 3. Set up the environment variables

- In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database
- In your settings.py file, import dj_database_url underneath the import for os

   import os
   import dj_database_url

- Update the DATABASES section to the following
  
            if 'DEV' in os.environ:
              DATABASES = {
                  'default': {
                      'ENGINE': 'django.db.backends.sqlite3',
                      'NAME': BASE_DIR / 'db.sqlite3',
                  }
              }
          else:
              DATABASES = {
                  'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
              }

- In your env.py file, add a new environment variable with the key set to DATABASE_URL, and the value to your ElephantSQL database URL

    os.environ['DATABASE_URL'] = "PostgreSQL URL"

- Temporarily comment out the DEV environment variable so that your IDE can connect to your external database

              import os

              os.environ['CLOUDINARY_URL'] = "cloudinary://..."
              os.environ['SECRET_KEY'] = "Z7o..."
              # os.environ['DEV'] = '1'
              os.environ['DATABASE_URL'] = "postgres://..."

- Back in your settings.py file, add a print statement to confirm you have connected to the external database

Add the following code to the bottom of the DATABASES section

        print('Connected to external database')

- In the terminal, -–dry-run your makemigrations to confirm you are connected to the external database

          python3 manage.py makemigrations --dry-run

- If you are, you should see the ‘connected’ message printed to the terminal
- Remove the print statement
- Migrate your database models to your new database
  
          python3 manage.py migrate

- Create a superuser for your new database

          python3 manage.py createsuperuser

- Follow the steps to create your superuser username and password

### 4 Confirming your app is connected to your external database

- On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”
- Click the Table queries button, select auth_user
- When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database

### 5. Preparing for deployment

- In the terminal of your IDE workspace, install gunicorn

      pip3 install gunicorn django-cors-headers

- Update your requirements.txt

 pip freeze --local > requirements.txt

- Create a Procfile

      release: python manage.py makemigrations && python manage.py migrate
      web: gunicorn drf_api.wsgi

- In your settings.py file, update the value of the ALLOWED_HOSTS variable to include your Heroku app’s URL

      ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']

- Add corsheaders to INSTALLED_APPS

        INSTALLED_APPS = [
            ...
            'dj_rest_auth.registration',
            'corsheaders',
            ...
        ]

- Add corsheaders middleware to the TOP of the MIDDLEWARE

          SITE_ID = 1
          MIDDLEWARE = [
              'corsheaders.middleware.CorsMiddleware',
              ...
          ]

- Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:

          if 'CLIENT_ORIGIN' in os.environ:
              CORS_ALLOWED_ORIGINS = [
                  os.environ.get('CLIENT_ORIGIN'),
              ]
          else:
              CORS_ALLOWED_ORIGIN_REGEXES = [
                  r"^https://.*\.gitpod\.io$",
              ]

- Enable sending cookies in cross-origin requests so that users can get authentication functionality

            else:
                CORS_ALLOWED_ORIGIN_REGEXES = [
                    r"^https://.*\.gitpod\.io$",
                ]

            CORS_ALLOW_CREDENTIALS = True

- To be able to have the front end app and the API deployed to different platforms, set the JWT_AUTH_SAMESITE attribute to 'None'. Without this the cookies would be blocked

            JWT_AUTH_COOKIE = 'my-app-auth'
            JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
            JWT_AUTH_SAMESITE = 'None'

- Remove the value for SECRET_KEY and replace with the following code to use an environment variable instead

            SECRET_KEY = os.getenv('SECRET_KEY')

- Set a NEW value for your SECRET_KEY environment variable in env.py, do NOT use the same one that has been published to GitHub in your commits
  
      os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")

- Set the DEBUG value to be True only if the DEV environment variable exists. This will mean it is True in development, and False in production

        DEBUG = 'DEV' in os.environ

- Comment DEV back in env.py
- Ensure the project requirements.txt file is up to date. In the IDE terminal of your DRF API project enter the following

        pip freeze --local > requirements.txt

- Add, commit and push your code to GitHub

### 6. Deploying to Heroku

- Heroku dashboard for your new app, open the Settings tab
- Add two more Config Vars:

  SECRET_KEY (you can make one up, but don’t use the one that was originally in the settings.py file!)

  CLOUDINARY_URL, and for the value, copy in your Cloudinary URL from your env.py file 

- Open the Deploy tab
- Under Deployment method, select GitHub
- Search for your repository and click connect
- Under Automatic deploys, click Enable Automatic Deploys
- Under Manual deploy, click Deploy Branch
- Once the build is complete, click View to open your app
- If you see the DRF API landing page, you have successfully deployed your app to Heroku

### Done - Congratulations!

## Credits
### Acknowledgements

- [Code Institute](https://codeinstitute.net/) for the course content and support
- [Stack Overflow](https://stackoverflow.com/) for the answers to many of my questions
- [W3Schools](https://www.w3schools.com/) for the answers to many of my questions
- [Django Documentation](https://docs.djangoproject.com/en/3.2/) for the answers to many of my questions
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/) for the answers to many of my questions
- [Cloudinary Documentation](https://cloudinary.com/documentation) for the answers to many of my questions
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/) for the answers to many of my questions
- My mentor Marcel for continuous helpful feedback.
- My fiancee for her support and encouragement.

[Back to top](#table-of-contents)