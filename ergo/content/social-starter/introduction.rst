:title: Introduction
:date: 2015-08-12 18:00
:series: starter
:series_index: 1
:tags: python, flask
:category: starter
:slug: starter-introduction
:authors: Anthony Plunkett
:summary: Guide to Building a Social Web Application with Flask.
:status: draft

Introduction
------------

If you step back at look at the crowd of social websites out there, they all share similar foundations and concepts.

-   They have users who can create core content, usually this content belongs to a category or is tagged.
-   In addition users can comment on, and favourite that content.
-   They can also usually follow other users and talk directly to one another.

Most sites you'll visit will fit to this rough shape,
some will call favourites up, or down voting (`Reddit`_),
sometimes the core content is a Photo (`Instagram`_) or a question (`Quora`_, `StackOverflow`_)).
If we step back a bit further, we can look at sites like `BuzzFeed`_ or `Slate`_ as fitting too--
in their case they have two classes of users, journalists who can create
core content and the general public who can comment upon it and share.

Visit a few of your favourite sites and see if they fit into this same concept, see if
they share the same foundations.

In this series, I'll detail my journey to build a web application that implements these
foundational ideas using the Flask framework and an assortment of extensions and packages
to make our project flow.

By the end you will be well placed to extend the project with your own ideas that give
your application

This guide is *not* the one-true guide on how to approach and complete a project.
While the `Zen of Python`_ says:


    "There should be one— and preferably only one —obvious way to do it."

    -- Zen of Python


That's not true, at all. The beauty of Flask (and other micro-frameworks) are
that they provide you with perfectly formed lego blocks
with which to build your project— you can use those block to build anything
from a simple drafty shack to an ornate cathedral.  If you prefer a more
structured approach, frameworks like Django or Pyramid provide a more structured
story for your project.


So.. What Shall We Build?
-------------------------

We're going to build a site that shares interesting content from around the web,
it might be a photo, a full editorial or just a link.  Think `Reddit`_, `MetaFilter`_
or `Digg`_.  Users can create posts that can be discussed by the other users.
Those posts and comments can be favourited by users.

Users will also be able to follow other users, so they can be alerted when those
users contribute to the site and they'll be able to send messages to one another.

Finally, we'll have a special type of user, the administrators, who will be
able to delete content and ban, or time-out users.

To get up and running quickly, we'll focus on the core functionality, then build outwards
to add some of the more fancy useful features in.

Prerequisites
-------------

Python runs on nearly every device out there, but development is generally easiest on
OSX or Linux.  Don't despair if you're a Windows user, I'll point you in the right
direction when I can, but for the most part when I'll be talking in the terminology
of a OSX user (e.g. launching a Terminal instead of opening a Command Line window).

Python 3.4.3
============

Python 3.4.3 is the current latest stable version of Python, it comes bundled with
the package manager and virtual environment tools that makes development easier.  All
the code in this project *should* work with Python 2.7.4 but I'd recommend 3.4.3
so we're on the same page.

Download and install it `from here <https://www.python.org/downloads/>`_.

PostgreSQL
==========

We're going to be storing our data for our application in PostgreSQL— It's a fantastic
database.  Often guides such as this one will just use SQLlite because it's built-in and
a little quicker to get going. Forget that. If you're ever wanting to put your site into
real production, you should be using the same database as you will when you go live.

Migrating from SQLlite to Postgres down the road *will* hurt you. SQLite allows
you to make data-model mistakes that will only become evident when you start using a real
database management system.

For OSX installing PostgreSQL is easy.  Just download `Postgres.app`_ and install it:

-   Download `Postgres.app`_
-   Move to `/Applications`
-   Double-Click to launch the Server.

For Windows users, it's just almost as `straight-forward from here <http://www.postgresql.org/download/windows/>`_.

A Development Environment
=========================

I'm going to assume you're using `Sublime`_ to edit and create your code.  I personally use PyCharm,
but will describe my steps using `Sublime`_ to open directories as projects etc.

Testing Our Setup
-----------------

Lets test that we've got everything installed correctly and we are all on the same page.

First open up a terminal window and type `Python3.4` and hit return.  If Python 3.4.3 is
installed correctly you should see::

    Python 3.4.3 (default, Aug 28 2015, 22:32:48)
    [GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin.
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Next up, lets test PostgreSQL is installed correctly.  Launch `Postgres` from Spotlight
and you should see a *"Welcome to Postgres"* dialog.  Click the `Open psql` button
to launch the psql terminal, and type in `select * from user;` and you should see
yourself listed as the current user.

If everything launched and worked great, then we are good to proceed.  If you ran into
any problems, investigate why and get the problems resolved, don't worry— we'll still
be here when you get back.

Getting Started
===============

Lets jump right in.  First we're going to need a place for our project to call home
so lets launch a terminal and create a folder and jump into it.  If you want to create
the folder in a different location, navigate there first.

    mkdir starter
    cd starter

We're going to quickly build the skeleton of our project in this folder, and populate
it shortly::

    touch config.py
    touch requirements.txt
    touch manage.py

    mkdir app
    cd app

    touch __init__.py
    touch models.py
    touch views.py

    mkdir static
    mkdir templates


By the end of that you should end up with a project directory that looks like:

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

Throughout the project we'll be adding more files in as we need.  When I talk
about adding a file to the project root, I mean adding them alongside the `requirements.txt`
and `config.py` files.

Virtual Environments
--------------------

We're going to want to play with our project in our own private sandbox,
called a virtual environment.  Essentially this lets us create a
little world for our project to live in that can't be hurt by future
(or past) projects we might have.

Open up a terminal and navigate to your project root directory then run:

.. code-block:: bash

    python -m venv world

Python will create a folder called `world` that will have it's very own
installation of Python.  We need to step into that world by activating
it from our terminal/command line:

.. code-block:: bash

    . world/bin/activate

For Windows users that means running the `activate.bat` file in
the `world/Scripts` directory:

.. code-block:: bash

    world/scripts/activate.bat

In either case, you'll notice your command prompt changes to indicate
that it's now standing within your virtual world.  If you open up
a new terminal window, that window won't be in the virtual world— so
you'll just need to remember to activate the world each time you
relaunch a terminal window.


Installing Packages
-------------------

So lets do a quick recap— we've got Python and PostgreSQL installed
and working. We've created out project skeleton and a virtual
environment where we can play with it. Next we're going to load in
the extensions and packages that will allow us to lean on the work
of others.

Open up `requirements.txt` in Sublime and add the following::

    flask
    flask-sqlalchemy
    flask-security
    flask-wtf
    flask-script
    flask-migrate
    psycopg2
    mixer
    arrow

Lets briefly go over what each package brings to the project:

-   **Flask** is our scaffolding for our project which handles all the requests
    for our application and routes them to the right places.
-   **Flask-SQLAlchemy** handles our data-model layer for us, it is our messenger
    to our database layer, handling a lot of the ugly, tedious work you might be used
    to when dealing with SQL.  You'll no longer have to covert from SQL types
    to Python types manually— SQLAlchemy will handle it all for us.  The
    **Flask-SQLAlchemy** extension adds a few little helpers which make some
    common tasks, like pagination really easy.
-   **Psycopg2** is the translator for our PostgreSQL database.  It's the person
    that SQLAlchemy needs to talk to, to send data to and from the database.
-   **Flask-Security** user authentication is a big piece of the puzzle when dealing
    with any modern web application.  **Flask-Security** makes it easy to ensure
    that only the right people are able to see the information they need to.
-   **Flask-WTF** handles our forms, it's a extension that builds on the great
    `wtforms`_ package and allows us to simply handle form validation and creation.
    It also works well with SQLAlchemy, allowing us to populate form elements
    directly from the database quickly and easily.
-   **Flask-Script** is our manager, we'll use it to carry out maintenance and
    tests on our application.  Think of **Flask-Script** as the command-line for
    your web-application.
-   **Flask-Migrate** though we won't use it at the start, **Flask-Migrate** is
    invaluable when you are knees deep in your project, it is an interface to
    `Alembic`_ which helps manage changes within your database.  Think of it as
    a version control for your database.
-   **Mixer** is a great tool for generating data for your application.  Once
    we've built up the model layer for our application, we'll use Mixer to populate
    it with test data.
-   **Arrow** is a Python library that gives you simple tools to manipulate and
    format dates, it's invaluable when building user interfaces where you'd like to
    say things like 'A few minutes ago'.

To install our packages, go to the project root directory and make sure (as always)
that you have activated the virtual environment.  Then simply do::

    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.3/bin
    python3.4 -m pip install -r requirements.txt

What we're doing is using the `pip` module that is now helpfully build into Python
to install all the packages we listed in our `requirements.txt` file.  The first line
lets pip know where we installed **Postgres.app** to.  If you're using a different
PostgreSQL version, you'll need to point it at the right place.

With a bit of luck, everything will install in a straightforward manner, and we can
proceed to actually beginning on constructing the building blocks of our application.


.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. _MetaFilter: https://www.metafilter.com/
.. _Digg: http://www.digg.com/
.. _Reddit: http://www.reddit.com/
.. _Quora: http://www.quora.com/
.. _StackOverflow: http://www.stackoverflow.com/
.. _BuzzFeed: http://www.buzzfeed.com/
.. _Instagram: http://www.instagram.com/
.. _Slate: http://www.slate.com/
.. _Postgres.app: http://www.postgresapp.com/
.. _Sublime: http://www.sublimetext.com/
.. _Pycharm: https://www.jetbrains.com/pycharm/