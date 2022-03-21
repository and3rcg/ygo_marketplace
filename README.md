# Yu-Gi-Oh! Marketplace

This website is just a personal project to guide my studies in Web development, and it is currently in a "work in progress" state. As of right now, it is in an extremely early state, and I intend to update it as I have free time.

## Objectives

-   Learn about the selected tech stack;
-   Develop my self-teaching capabilities;
-   Start off my Web developer portfolio;
-   Getting familiar with a Linux development environment (using WSL), as well as Git.

## Tech stack

-   Python 3.9.10 (with Django 4.0.2 and Django REST Framework 3.13.1);
-   Node.js 17.5.0 (with React 17.0.2);
-   PostgreSQL database v.14
-   Docker.

## Installation instructions

Since the `SECRET_KEY` in `settings.py` is private, it is recommended to anybody who wishes to run this app locally to create a `.env` file in the root folder of this project, then add the line `SECRET_KEY = '<your secret key here>'`. To generate a secret key, it is recommended that users get a secret key from an app such as https://djecrety.ir\.  
After the secret key has been added to the local project, run the app with:

```
docker-compose up -d
```

Once the application is up and running, the website should be ready to navigate, but there won't be any cards. In order to add the cards from the YGOPRODeck API, use the command:

```
docker exec backend python manage.py updatedb
```

Or you can just log into the container and run `python manage.py updatedb` from there.
