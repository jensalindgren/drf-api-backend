# Gymhub

## Project Goals

This project provides a Django Rest Framework API for a gym network. It has also a React frontend to interact with the API.

Gymhub is a platform that allows it gym members to post comment and get information about the gym they are subscribed to. It also allows the gym owners to manage their gym and their members trough the platform.

## Table of Contents
- [Gymhub](#gymhub)
  - [Project Goals](#project-goals)
  - [Table of Contents](#table-of-contents)
  - [Planning](#planning)
  - [User Stories](#user-stories)
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
  - [Technologies Used](#technologies-used)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)




## Planning

Planning was done with user stories for the here for the backend. I started to lay up the most important models and their relationships. I also started to think about the endpoints and the serializers. I also started to think about the frontend and the components I would need.

## User Stories

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

### Likes

### Followers

### Upvotes

### Events


## Testing

## Technologies Used

## Deployment to Heroku

## Credits

## Acknowledgements