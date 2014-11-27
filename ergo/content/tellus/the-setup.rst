:title: Helpful Flask Extensions
:date: 2014-11-27 19:00
:series: tellus
:tags: python, flask
:category: tellus
:slug: tellus-setup
:authors: Anthony Plunkett
:summary: Helpful Flask Extensions

Flask isn't just a project, it's an ecosystem.  You *can* choose to implement
everything yourself, or you can sit back and realise that smarter people
then you are out there, and use the opportunity to stand on their shoulders
and let their hard work make your life easier.

Below is a brief introduction to the extensions I'm planning to use on this
project.

Flask-SQLAlchemy
================

SQLAlchemy is essentially magic.  The ORM feature of SQLAlchemy allows you
to abstract away your SQL database, it becomes a powerful interface that
allows you to talk directly with the Python objects without having to
translate things back and forth.

Flask-Security
==============

User authentication and security is a big piece of the puzzle in any modern
application, you need to handle registrations, log-ins, password resets.  You
need to handle roles, so you can give admins extra rights, and you need
to control where those users can go, and what they can do.

It's complicated, and worse, it's boring-- luckily, it's pretty much
all handled for us with Flask-Security, which stitches together a number
of other Flask extensions into something that's more then the sum of
it's parts.

Flask-WTF
=========

Another pain in web development is handling forms, you need to worry about
attack vectors from external sites, double submissions of content.  Loading
data into forms, validating that data-- yawn.  Again, Flask-WTF makes that
much nicer and it works perfectly with SQLAlchemy.

Flask-Script
============

Flask-Script helps you do your book-keeping, this is especially helpful when
you're developing, and you're constantly deleting, creating and populating
your database.  Flask-Script lets us easily create simple functions to control
our application from the command line.

Flask-Testing
=============

We talked about our TDD stories in the last article.  Flask-Testing lets us
build those stories and test our functionality.