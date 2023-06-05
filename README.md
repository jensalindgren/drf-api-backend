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
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Packages](#packages)
    - [Tools](#tools)
  - [Deployment to Heroku](#deployment-to-heroku)
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

| Application | Endpoint                  | Expected Result                                                                                                                                            | Pass/Fail |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Profiles    | profiles/                 | Returns a list of all the profiles in the database ordered by creation date                                                                                | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user isn't the owner of the profile, they can't edit or delete it      | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user is the owner of the profile, they can edit and delete it          | Pass      |
| Comments    | comments/                 | Return a list of all the comments in order of creation date                                                                                                | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values                                                                                   | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and the owner can edit and delete the comment                                     | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and if the user isn't the owner of the comment, they can't edit or delete i       | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and even if the user is a staff member, they can't edit and delete it             | Pass      |
| Upvotes     | upvotes/                  | Returns a list of all the current upvotes in the database                                                                                                  | Pass      |
| Upvotes     | upvotes/                  | If a user is logged out they are not able to upvote a post                                                                                                 | Pass      |
| Upvotes     | upvotes/<int:pk>/         | Returns a single upvote with a correct ID and a list of all it's values                                                                                    | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is the owner of the upvote, they can delete the upvote and it will delete it from the champion and decrease the upvote_count by 1              | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote, they are unable to delete the upvote                                                                           | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote but is a staff member, they are unable to delete the upvote                                                     | Pass      |

[Back to top](#gymhub)

## Technologies Used

### Languages

Python a high level programming language was used to create the backend of the application.

### Libraries

Django a python web framework was used to create the backend of the application.
Django Rest Framework was used to create the API endpoints for the application.

### Packages

- [asgiref](https://pypi.org/project/asgiref/) - A standard for Python asynchronous web apps and servers to communicate with each other,
- [black](https://pypi.org/project/black/) - A Python code formatter
- [click](https://pypi.org/project/click/) - A Python package for creating command line interfaces
- [cloudinary](https://pypi.org/project/cloudinary/) - Easily integrate your application with Cloudinary
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication securely in Django Rest Framework
- [Django](https://pypi.org/project/Django/) - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - package that facilitates integration with Cloudinary by implementing Django Storage API
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Adds Cross-Origin Resource Sharing (CORS) headers to responses.
- [django-extensions](https://pypi.org/project/django-extensions/) - Collection of global custom management extensions for the Django Framework.
- [django-filter](https://pypi.org/project/django-filter/) - Declaratively add dynamic QuerySet filtering from URL parameters.
- [djangorestframework](https://pypi.org/project/djangorestframework/) - A powerful and flexible toolkit for building Web APIs.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server for UNIX.
- [idna](https://pypi.org/project/idna/) - Support for the Internationalized Domain Names in Applications (IDNA) protocol
- [mypy-extensions](https://pypi.org/project/mypy-extensions/) - Defines extensions to the standard “typing” module that are supported by the mypy type checker and the mypyc compiler.
- [oauthlib](https://pypi.org/project/oauthlib/) - Implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [pathspec](https://pypi.org/project/pathspec/) - Utility library for pattern matching of file paths
- [Pillow](https://pypi.org/project/Pillow/) - Adds image processing capabilities to your Python interpreter
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python
- [pycodestyle](https://pypi.org/project/pycodestyle/) - A tool to check your Python code against some of the style conventions in PEP 8.
- [PyJWT](https://pypi.org/project/PyJWT/) - Library for encoding and decoding JSON Web Tokens (JWT)
- [python3-openid](https://pypi.org/project/python3-openid/) - Python OpenID library
- [pytz](https://pypi.org/project/pytz/) - Allows accurate and cross platform timezone calculations
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [urllib3](https://pypi.org/project/urllib3/) - A powerful, user-friendly HTTP client for Python

### Tools

- [VSCode](https://code.visualstudio.com/) - IDE used to develop the application.
- [GitHub](https://github.com/) - Used to host and deploy the website as well as manage the project.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files .
- [Git](https://git-scm.com/) - Version control
- [Heroku](https://www.heroku.com/) - Deployment
- [ElephantSQL](https://www.elephantsql.com/) - Provides a browser tool for SQL queries where you can create, read, update and delete data directly from your web browser.
- [CI PEP8 Linter](https://pep8ci.herokuapp.com/#) - Used to check the Python code for any linting issues

[Back to top](#gymhub)
## Deployment to Heroku

## Credits

## Acknowledgements