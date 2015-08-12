:title: The Blank Canvas
:date: 2015-08-12 18:00
:series: starter
:series_index: 2
:tags: python, flask
:category: starter
:slug: the-blank-canvas
:authors: Anthony Plunkett
:summary: Starting the Project


For the purposes of simplicity, I'm going to presume that you have
Python 3.4.3 installed on your computer.

Lets first create a directory called `starter` to house our new project.
We'll also create a number of subdirectories and empty files which will
act as the skeleton of our application

..  image:: /images/starter/starter-directories.png
    :alt: Starter Skeleton


Lets walk through the files we have just created to give you an overview
for their future purpose:

-   **requirements.txt**— Python lets us easily bring in packages that
    other smart people have made, we'll use these to help us use our
    database, or user-authentication, and many more features.  We can
    list the names of the packages we need, and tell Python to install
    them for us automatically.

-   **manage.py**— We'll use this file to manage our application.  We'll
    use it to run our development web-server, create our database and
    populate some test data into our application to make development easier.

-   **config.py**— We'll use this file to configure the larger pieces of our
    application, like telling it where our database is, and other important
    settings.

-   **views.py**— View's are windows into our application.  User's access
    these views by going to a webpage, which triggers the view into generating
    the data required to build a webpage.

-   **models.py**— The objects that give life to our application live here,
    we will have a `User` model to represent users of our site, and a `Post`
    and `Comment` model to represent their actions.  These models create
    and interact with our database to make the magic happen.

-   **__init__.py**— Think of this file as the index of our application, it's
    a special filename that Python recognises to know that the `app` folder is
    a package.  Think of it as the bridge that brings all the views and models
    together to make the application unified.

-   **static**— This folder holds our data that doesn't change, that could
    be our CSS files, our Javascript scripts as well as images like logo's.

-   **templates**— Our templates live in this directory.  Templates are used
    by our views to render out complete webpages using the data the view grabs
    from the data-models.
