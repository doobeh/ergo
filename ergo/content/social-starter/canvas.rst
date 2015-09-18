:title: Foundation Prerequisites
:date: 2015-09-18 12:44
:series: fountain
:series_index: 3
:tags: python, flask
:category: fountain
:slug: fountain-prerequisites
:authors: Anthony Plunkett
:summary: Setting up your environment for the Foundation project.
:status: published

Python runs on nearly every device out there, but development is generally easiest on
OSX or Linux. Don't despair if you're a Windows user, I'll point you in the right
direction when I can, but for the most part when I'll be talking in the terminology
of a OSX user (e.g. launching a Terminal instead of opening a Command Line window).

Python 3.4.3
============

Python 3.4.3 is the current latest stable version of Python, it comes bundled with
the package manager and virtual environment tools that makes development easier. All
the code in this project *should* work with Python 2.7.4 but I'd recommend 3.4.3
so we're on the same page.

Download and install it `from here <https://www.python.org/downloads/>`_.

PostgreSQL
==========

We're going to be storing our data for our application in PostgreSQL— It's a fantastic
database. Often guides such as this one will just use SQLlite because it's built-in and
a little quicker to get going. Forget that. If you're ever wanting to put your site into
real production, you should be using the same database as you will when you go live.

Migrating from SQLlite to Postgres down the road *will* hurt you. SQLite allows
you to make data-model mistakes that will only become evident when you start using a real
database management system.

For OSX installing PostgreSQL is easy. Just download `Postgres.app`_ and install it:

-   Download `Postgres.app`_
-   Move to `/Applications`
-   Double-Click to launch the Server.

For Windows users, it's almost as `straight-forward from here <http://www.postgresql.org/download/windows/>`_.

A Development Environment
=========================

I'm going to assume you're using `Sublime`_ to edit and create your code. I personally use PyCharm,
but generally this doesn't matter at all.

Testing Our Setup
-----------------

Lets test that we've got everything installed correctly and we are all on the same page.

First open up a terminal window and type `Python3.4` and hit return. If Python 3.4.3 is
installed correctly you should see::

    Python 3.4.3 (default, Aug 28 2015, 22:32:48)
    [GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.53)] on darwin.
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Next up, lets test PostgreSQL is installed correctly. Launch `Postgres` from Spotlight
and you should see a *"Welcome to Postgres"* dialog. Click the `Open psql` button
to launch the psql terminal, and type in `select * from user;` and you should see
yourself listed as the current user.  We'll use that username when we later
get Python talking to this database, so keep it in mind.

If everything launched and worked great, then we are good to proceed. If you ran into
any problems, investigate why and get the problems resolved, don't worry— we'll still
be here when you get back.

A Place to Call Home
--------------------

First we're going to need a place for our project to call home
so lets launch a terminal and create a folder and jump into it. If you want to create
the folder in a different location, navigate there first.  By default opening
a terminal will place you into your user-home.  Personally I have a `development`
directory within my user-home that I then place all my projects into to keep things tidy.

.. code-block:: bash

    mkdir fountain
    cd fountain

Virtual Environments
--------------------

We're going to want to play with our project in our own private sandbox,
called a virtual environment. Essentially this lets us create a
little world for our project to live in that can't be hurt by future
(or past) projects we might have.

Open up a terminal and navigate to your project root directory then run:

.. code-block:: bash

    python -m venv world

Python will create a folder called `world` that will have it's very own
installation of Python. We need to step into that world by activating
it from our terminal/command line:

.. code-block:: bash

    . world/bin/activate

For Windows users that means running the `activate.bat` file in
the `world/Scripts` directory:

.. code-block:: bash

    world/scripts/activate.bat

In either case, you'll notice your command prompt changes to indicate
that it's now standing within your virtual world. If you open up
a new terminal window, that window won't be in the virtual world— so
you'll just need to remember to activate the world each time you
relaunch a terminal window.

Next we'll create the skeletal structure of our application and install
the libraries that will help us develop our application in a smooth
manner.

.. _Sublime: http://www.sublimetext.com/
.. _Postgres.app: http://www.postgresapp.com/