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

We're going to be storing our data for our application in PostgreSQL-- It's a fantastic
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
any problems, investigate why and get the problems resolved.










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