:title: Helpful Flask Extensions
:date: 2014-11-27 19:00
:series: tellus
:series_index: 2
:tags: python, flask
:category: tellus
:slug: tellus-setup
:authors: Anthony Plunkett
:summary: Helpful Flask Extensions

Flask isn't just a project, it's an ecosystem.  You *can* choose to implement
everything yourself, or you can sit back and realise that smarter people
then you are out there, they've already dug through the weeds and built
something great.  Stand on their shoulders and let their efforts make your
life easier.

Below is a whirlwind introduction to the extensions I'm planning to use on this
project.  All of these projects have great quick-start guides that get you up
to speed pretty quickly.  Flask-Security is the most complex because it's
solving a complex problem, but it's well worth your time to take a break
from this guide and have a good skim of their documentation.

Flask-SQLAlchemy
================

    "Any sufficiently advanced technology is indistinguishable from magic."

    -- Arthur C. Clarke


`SQLAlchemy`_ is essentially magic.  The Object Relational Mapper (ORM) allows
you to marry your python objects that represent your business logic (Users,
Articles, Payments, etc) to your database.  That allows your database to
fade into the background and out of your thoughts.  SQLAlchemy handles
all the complexities of translating the database layer into your Python
objects.

`Flask-SQLAlchemy`_ takes SQLAlchemy and adds a few handy shortcuts that lets
us save a bit of code when using it with Flask.

For instance, if I wanted to grab a specific user, and then print all the
article titles they've published, I would likely do something like:

.. code-block:: python

    user = User.query.filter_by(username='Susan').first()
    for article in user.articles:
        print article.title

It's as easy as that— no SQL involved.  Magic.


Flask-Security
==============

User authentication and security is a big piece of the puzzle in any modern
application, you need to handle registrations, log-ins, password resets.
Roles needs to be managed so you can give admins extra rights, and you need
to control where those users can go, and what they can do.

It's complicated, and worse, it's boring— luckily, it's pretty much
all handled for us with `Flask-Security`_, which stitches together a number
of other Flask extensions into something that's more then the sum of
it's parts.

Flask-WTF
=========

Another pain in web development is handling forms, you need to worry about
attack vectors from external sites, double submissions of content.  Loading
data into forms, validating that data— yawn.  Again, `Flask-WTF`_ makes that
much nicer and it works perfectly with SQLAlchemy, which makes populating forms
based off your models simple.

Flask-Script
============

`Flask-Script`_ helps you do your bookkeeping, this is especially helpful when
you're developing, and you're constantly deleting, creating and populating
your database.  Flask-Script lets us easily create simple functions to control
our application from the command line.

Flask-Testing
=============

We talked about our TDD stories in the last article.  `Flask-Testing`_ lets us
build those stories and test our functionality.

.. _Flask-Script: http://flask-script.readthedocs.org/en/latest/
.. _Flask-Security: https://pythonhosted.org/Flask-Security/
.. _Flask-SQLAlchemy: https://pythonhosted.org/Flask-SQLAlchemy/
.. _Flask-Testing: https://pythonhosted.org/Flask-Testing/
.. _Flask-WTF: https://flask-wtf.readthedocs.org/en/latest/
.. _SQLAlchemy: http://www.sqlalchemy.org/