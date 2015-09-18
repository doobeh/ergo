:title: The Project
:date: 2015-08-12 18:00
:series: fountain
:series_index: 2
:tags: python, flask
:category: fountain
:slug: fountain-project-scope
:authors: Anthony Plunkett
:summary: Guide to Building a Social Web Application with Flask - Project Scope
:status: published

So.. What Shall We Build?
-------------------------

We're going to build a site that shares interesting content from around the web,
it might be a photo, a full editorial or just a link. Think `Reddit`_, `MetaFilter`_
or `Digg`_. Users can create posts that can be discussed by the other users.
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

For Windows users, it's just almost as `straight-forward from here <http://www.postgresql.org/download/windows/>`_.

A Development Environment
=========================

I'm going to assume you're using `Sublime`_ to edit and create your code. I personally use PyCharm,
but will describe my steps using `Sublime`_ to open directories as projects etc.

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
yourself listed as the current user.

If everything launched and worked great, then we are good to proceed. If you ran into
any problems, investigate why and get the problems resolved, don't worry— we'll still
be here when you get back.

Getting Started
===============

Lets jump right in. First we're going to need a place for our project to call home
so lets launch a terminal and create a folder and jump into it. If you want to create
the folder in a different location, navigate there first.

.. code-block:: bash

    mkdir fountain
    cd fountain

We're going to quickly build the skeleton of our project in this folder, and populate
it shortly::

    touch config.py
    touch requirements.txt
    touch manage.py

    mkdir app
    cd app

    touch __init__.py
    touch core.py
    touch models.py
    touch views.py

    mkdir static
    mkdir templates


By the end of that you should end up with a project directory that looks like:

..  image:: /images/fountain/fountain-directories.png
    :alt: Fountain Skeleton

Lets walk through the files we have just created to give you an overview
for their future purpose:

-   **requirements.txt**— Python lets us easily bring in packages that
    other smart people have made, we'll use these to help us use our
    database, or user-authentication, and many more features. We can
    list the names of the packages we need, and tell Python to install
    them for us automatically.

-   **manage.py**— We'll use this file to manage our application. We'll
    use it to run our development web-server, create our database and
    populate some test data into our application to make development easier.

-   **config.py**— We'll use this file to configure the larger pieces of our
    application, like telling it where our database is, and other important
    settings.

-   **views.py**— View's are windows into our application. User's access
    these views by going to a webpage, which triggers the view into generating
    the data required to build a webpage.

-   **models.py**— The objects that give life to our application live here,
    we will have a `User` model to represent users of our site, and a `Post`
    and `Comment` model to represent their actions. These models create
    and interact with our database to make the magic happen.

-   **__init__.py**— Think of this file as the index of our application, it's
    a special filename that Python recognises to know that the `app` folder is
    a package.

-   **core.py**— In here we'll set up the actual Flask app, and bring all
    the pieces together into one central place.

-   **static**— This folder holds our data that doesn't change, that could
    be our CSS files, our Javascript scripts as well as images like logo's.

-   **templates**— Our templates live in this directory. Templates are used
    by our views to render out complete webpages using the data the view grabs
    from the data-models.

Throughout the project we'll be adding more files in as we need. When I talk
about adding a file to the project root, I mean adding them alongside the `requirements.txt`
and `config.py` files.

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
    to when dealing with SQL. You'll no longer have to covert from SQL types
    to Python types manually— SQLAlchemy will handle it all for us. The
    **Flask-SQLAlchemy** extension adds a few little helpers which make some
    common tasks, like pagination really easy.
-   **Psycopg2** is the translator for our PostgreSQL database. It's the person
    that SQLAlchemy needs to talk to, to send data to and from the database.
-   **Flask-Security** user authentication is a big piece of the puzzle when dealing
    with any modern web application. **Flask-Security** makes it easy to ensure
    that only the right people are able to see the information they need to.
-   **Flask-WTF** handles our forms, it's a extension that builds on the great
    `wtforms`_ package and allows us to simply handle form validation and creation.
    It also works well with SQLAlchemy, allowing us to populate form elements
    directly from the database quickly and easily.
-   **Flask-Script** is our manager, we'll use it to carry out maintenance and
    tests on our application. Think of **Flask-Script** as the command-line for
    your web-application.
-   **Flask-Migrate** though we won't use it at the start, **Flask-Migrate** is
    invaluable when you are knees deep in your project, it is an interface to
    `Alembic`_ which helps manage changes within your database. Think of it as
    a version control for your database.
-   **Mixer** is a great tool for generating data for your application. Once
    we've built up the model layer for our application, we'll use Mixer to populate
    it with test data.
-   **Arrow** is a Python library that gives you simple tools to manipulate and
    format dates, it's invaluable when building user interfaces where you'd like to
    say things like 'A few minutes ago'.

To install our packages, go to the project root directory and make sure (as always)
that you have activated the virtual environment. Then simply do::

    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.3/bin
    python3.4 -m pip install -r requirements.txt

What we're doing is using the `pip` module that is now helpfully build into Python
to install all the packages we listed in our `requirements.txt` file. The first line
lets pip know where we installed **Postgres.app** to. If you're using a different
PostgreSQL version, you'll need to point it at the right place.

With a bit of luck, everything will install in a straightforward manner, and we can
proceed to actually beginning on constructing the building blocks of our application.

The Data Model
--------------

What is a data model? We've talked about how web applications have core foundations
that are common, User's, Posts, Comments and more. The data-model is the representation
of those elements and importantly how they relate to one another.

A robust data-model makes everything else simple. We're using SQLAlchemy
to define our data-models and the relationship between them. Once we've
defined them, we'll load some test data into it, and explore it to
see if our expectations match reality.

If you're new to SQLAlchemy, have a read of `my post showing how it can be
used <{filename}../2015/01/sqlalchemy-cheatsheet.rst>`_ so you're not
entirely at a loss as we go on.

Lets first think about the general models we'll need and their relationships
to each other

-   **User**
-   **Role**— Some users have special roles that grant them extra functionality.
-   **Post**— The core content of the site.
-   **Comment**
-   **Message**— To represent the private messages passed between users
-   **Favourite**— Store user's favourites.
-   **Category**— The site will have several categories (Tech, Literature, News..)
    that Post's can be assigned to.
-   **Tag**— A post can have several tags that allows better searching and
    discovery of related posts.

The next step is to map the connections between them. I find that easiest on
paper, then translate that to code. Below is my sketch of the relations
using crows-foot notation (the splayed connections indicate a 'many' while
the single connection indicates the 'one' side of the relation).

..  image:: /images/fountain/fountain-erd.jpg
    :alt: Fountain ERD Sketch

You'll see a few M2M relationships, including the self-referential one where
users' are connect to themselves. For each of these relationships we'll use
a join table to enable them, then use the magic of SQLAlchemy to make the
relationship seamless.

Lets start by opening up `models.py` in our editor and defining our basic
User and Role models.

.. code-block:: python

    from flask_ext.sqlalchemy import SQLAlchemy
    from flask_ext.security import UserMixin, RoleMixin

    db = SQLAlchemy()

    roles_users = db.Table(
        'roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id'), index=True),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'), index=True)
    )

    class Role(db.Model, RoleMixin):
        __tablename__ = 'role'
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(80), unique=True, index=True)

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name


    class User(db.Model, UserMixin):
        __tablename__ = 'user'
        id = db.Column(db.Integer(), primary_key=True)
        username = db.Column(db.String(), index=True, nullable=False)
        password = db.Column(db.String(), nullable=False)
        email = db.Column(db.String(), nullable=False)
        active = db.Column(db.Boolean(), default=False, nullable=False)
        status = db.Column(db.Integer())
        status_changed = db.Column(db.DateTime())
        confirmed_at = db.Column(db.DateTime())
        roles = db.relationship('Role', secondary=roles_users,
                                backref=db.backref('users', lazy='dynamic'))

        def __repr__(self):
            return self.username

The first thing you'll notice is we're using a `UserMixin` object from Flask-Security.
This is a helper object that has some of the methods and attributes required to
allow all the features of Flask-Security to work.

We then define our `roles_users` table which will be the register of our many-to-many
joins between our `User` object and it's potentially many `Roles`. Most of the
attributes on `User` are self-explanatory. We'll set `User.active = True` when
they confirm their email address so we know to allow them to login to the site.
For now I've allocated `User.status` as the place
where I'll mark if a user is banned, or has cancelled their account.
To give us some flexibility I've also added a `User.status_date` which we
could use in tandem with the status to perhaps only temporarily ban a user.

Lets carry on an add the rest of the models:

.. code-block:: python

    post_tags = db.Table(
        'post_tags',
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
    )

We know we've got another M2M join between our `Post` and `Tag` objects. So
we create another association table to act as the journal for these items.

.. code-block:: python

    class Tag(db.Model):
        __tablename__ = 'tag'
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(50), unique=True)

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    class Category(db.Model):
        __tablename__ = 'category'
        id = db.Column(db.Integer(), primary_key=True)
        title = db.Column(db.String(), nullable=False, unique=True)
        slug = db.Column(db.String(), nullable=False, unique=True)

        def __repr__(self):
            return self.title

Our `Tag` object is straight-forward, we'll define the relationship between a `Tag`
and a `Post` when we define the `Post` object. The same is true of the `Category`
object.

.. code-block:: python

    class Favourite(db.Model):
        __tablename__ = 'favourite'
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), index=True)
        comment_id = db.Column(db.Integer(), db.ForeignKey('comment.id'), index=True)
        post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), index=True)

The `Favourite` object is a little more interesting. I've decided to track
favourites for both posts and comments in this single model. I was torn by this,
usually I would have created two objects, `CommentFavourite` and `PostFavourite`.

.. code-block:: python

    class Post(db.Model):
        __tablename__ = 'post'
        id = db.Column(db.Integer(), primary_key=True)
        title = db.Column(db.String(), nullable=False)
        link = db.Column(db.String())
        summary = db.Column(db.Text())
        content = db.Column(db.Text())
        dt = db.Column(db.DateTime(), nullable=False, index=True, default=datetime.now)
        deleted = db.Column(db.Boolean())
        favourites = db.relationship('Favourite', backref=db.backref('post'))

        category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
        category = db.relationship('Category', backref='posts')

        author_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
        author = db.relationship('User', backref='posts')

        tags = db.relationship('Tag', secondary=post_tags, backref=db.backref(
            'posts', lazy='dynamic', order_by='Post.dt.desc()')
        )

        def get_tags_csv(self):
            return ",".join(x.name for x in self.tags)

        def set_tags_csv(self, value):
            new = (x.lower() for x in value.strip(',; ').split(','))
            self.tags = []
            for tag in new:
                existing_tag = Tag.query.filter_by(name=tag).first()
                if existing_tag:
                    self.tags.append(existing_tag)
                else:
                    t = Tag(tag.strip())
                    self.tags.append(t)
            db.session.commit()

        tags_csv = property(get_tags_csv, set_tags_csv)

        def __repr__(self):
            return '{}: {}'.format(self.id, self.title)


Okay, a lot going on here. We've finally defined our relationships that interact with the `Post` model.
The important aspect is the defined `backrefs` these allow the magic that truly makes SQLAlchemy shine by
allowing us to jump between the relationships. For example, lets say we wanted to find all the posts
that were authored by `alice`:

.. code-block:: python

    user = User.query.filter_by(username='alice').first()
    for post in user.posts:
        print(post)

Would give us a listing of each of Alice's posts. We also have a `get_tags_csv` and `set_tags_csv` to
act as a manager for our `Tag` creation. The reason for this is that when we add a new post, we'd like
the user to add these meta-data tags to the post, but if a tag *already* exists in our system, we want
to use that existing one, not simply create a duplicate one.
The `set_tags_csv` does that check for us, when we supply it a string of tags like `tech, music, love`
it will break that string down into the three words, then check the database if they exist before
assigning them to the `Post`.

Finally lets get the `Comment` object created— we've already build the relationship for it in the `Post`
object but because we quoted the class, it doesn't matter that we defined it later.

.. code-block:: python

    class Comment(db.Model):
        __tablename__ = 'comment'

        id = db.Column(db.Integer(), primary_key=True)
        content = db.Column(db.Text())
        dt = db.Column(db.DateTime(), index=True, default=datetime.now)

        post_id = db.Column(db.Integer(), db.ForeignKey('post.id'), index=True)
        post = db.relationship('Post', backref=db.backref('comments', lazy='dynamic', order_by='Comment.dt.asc()'))

        user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), index=True)
        user = db.relationship('User', backref=db.backref('comments', lazy='dynamic'))

        favourites = db.relationship('Favourite', backref=db.backref('comment'))

        def __repr__(self):
            return '<Comment {} by {} on {} @ {}>'.format(
                self.id,
                self.user,
                self.post,
                self.dt.strftime("%Y-%m-%d %H:%M")
            )

We've added a slightly more interesting `__repr__` for this object. A `__repr__` is just the
representation of the object when it's rendered as a string (e.g. when we `print` it when
we're playing with it on out terminal or use it in our templates later).

Building the Core Flask App
---------------------------

Let's now get a small working application working, so we can have a central place to shape
our growing application.

Create the Database
===================

First we're going to need a database to communicate with. We've already installed PostgreSQL
but we have yet to actually create a database for our application's data to call home. So launch
the Postgres app, click the `open psql` button and enter the following command::

    CREATE DATABASE fountain;

This will create the blank database to work with. SQLAlchemy will do the job of creating the
tables. Next lets open up  our `config.py` file and add the connection details for our
database so SQLAlchemy will know where to go for our data. We're also going to set our
secret key which Flask and it's extensions use to handle some of our encryption for us::

    SQLALCHEMY_DATABASE_URI = 'postgres://user@127.0.0.1:5432/fountain'
    SECRET_KEY = 'SUPER_SECRET_DO_NOT_SHARE'

The Heart of our Application : core.py
======================================

Now lets flip over to our `core.py` and create our basic application by entering the following code:

.. code-block:: python

    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy
    from flask.ext.security import Security, SQLAlchemyUserDatastore
    from app.models import User, Role

    def create_app(config_filename):
        factory_app = Flask(__name__)
        factory_app.config.from_pyfile(config_filename)
        return factory_app

    app = create_app('../config.py')

    #: Flask-SQLAlchemy extension instance
    db = SQLAlchemy()
    db.init_app(app)

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    @app.route('/')
    def home():
        return 'Home'

This is the core of our application. We've defined a Flask application
using a factory pattern— the reason for this is to decouple our application
slightly which saves us running into trouble with circular imports.

Then we've registered our SQLAlchemy and Security extensions against our
application, specifying that the models we want the Security extension to
use are the ones we created over in our `models.py` file.

Finally we created a very stupid view, so when we run our application and
access the home page, we'll just get "Home" displayed to us. We'll throw
out this view when get get to building the real interfaces for our project.

The Management Interface : manage.py
====================================

Next we're going to start building the technical interface to our application,
this is how we're going to explore our models and do more maintenance tasks.
Open up the `manage.py` file and enter the following:

.. code-block:: python

    from flask.ext.script import Manager, Shell
    from app.models import User, Role, Post, Comment, Favourite, Tag, Category, db
    from app.core import app

    def _make_context():
        return dict(
            app=app, db=db,
            User=User, Post=Post, Role=Role,
            Comment=Comment, Favourite=Favourite,
            Tag=Tag, Category=Category
        )

    manager = Manager(app)
    manager.add_command('shell', Shell(make_context=_make_context))

    @manager.command
    def nuke():
        db.drop_all()
        db.create_all()
        print('Database Created')

    if __name__ == '__main__':
        manager.run()

We've initialized the `Manager` extension against our app, in the very same way
we did with Flask-SQLAlchemy and Flask-Security and defined a couple of commands:

-   **shell**— this allows us to quickly dive into our application in a state where
    we can immediately start playing around. The `_make_context` helps us out
    here by letting us inject all those values into our shell context. In short,
    this means we don't have to `from app.models import ...` all the models
    we want to play with every time we dive into the shell.
-   **nuke**— This tells our SQLAlchemy database object to destroy, then create
    all the tables in our application.

Lets test out the management interface. Launch a terminal, activate the virtual
environment and go to the project root directory. We're going to create our database
and then launch into a shell. First the database:

.. code-block:: bash

    python manage.py nuke

And assuming you created your database successfully earlier and didn't type in the
connection string incorrectly in `config.py` you should get a message back saying
`Database Created`.

Congratulations, we can now start to explore our data models. Lets launch into the
shell for our application:

.. code-block:: bash

    python manage.py shell

You'll be taken to a python shell, that's already configured for our application.
Lets add `Role` called 'admin', then add a `User` called 'alice' and assign that
Role to her:

.. code-block:: pycon

    >>> r = Role(name='admin')
    >>> u = User(username="alice", password="password", email="alice@example.com", active=True)
    >>> u.roles.append(r)

    Lets add the new user to the SQLAlchemy database session:
    >>> db.session.add(u)

    # then tell the database to save the data:
    >>> db.session.commit()

That's great for one user, but is going to get tiresome to add enough users, posts, categories,
tags, comments. We can turn to the Mixer library to handle it all for us. Lets open up
`manage.py` again and add a new `populate` command:

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. _MetaFilter: https://www.metafilter.com/
.. _Digg: http://www.digg.com/
.. _Reddit: http://www.reddit.com/
.. _Quora: http://www.quora.com/
.. _Stackoverflow: http://www.stackoverflow.com/
.. _BuzzFeed: http://www.buzzfeed.com/
.. _Instagram: http://www.instagram.com/
.. _Slate: http://www.slate.com/
.. _Postgres.app: http://www.postgresapp.com/
.. _Sublime: http://www.sublimetext.com/
.. _Pycharm: https://www.jetbrains.com/pycharm/
.. _Alembic: https://alembic.readthedocs.org/en/latest/
.. _wtforms: http://wtforms.readthedocs.org/en/latest/