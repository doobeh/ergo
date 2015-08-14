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
act as the skeleton of our application.

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


Virtual Environments
====================

We're going to want to play in our own private sandbox, called a virtual
environment.  Essentially this lets us create a little world for our project
to live in that can't be hurt by future projects we create.

Open up a terminal and navigate to your `starter` directory then run:

.. code-block:: bash

    python -m venv world

Python will create a folder called world that will have it's very own
installation of Python.  We need to step into that world by activating
it from our terminal/command line.
For Windows users that means running the `activate.bat` file in
the `world/Scripts` directory:

.. code-block:: bash

    world/scripts/activate.bat

For everyone else, you'll do something like:

.. code-block:: bash

    . world/bin/activate

In either case, you'll notice your command prompt changes to indicate
that it's now standing within your virtual world.  If you open up
a new terminal window, that window won't be in the virtual world— so
you'll just need to remember to activate the world for it each time.
