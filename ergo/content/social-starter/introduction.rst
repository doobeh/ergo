:title: Introduction
:date: 2015-08-12 18:00
:series: fountain
:series_index: 1
:tags: python, flask
:category: fountain
:slug: fountain-introduction
:authors: Anthony Plunkett
:summary: Guide to Building a Social Web Application with Flask.
:status: published


If you step back at look at the crowd of social websites out there, they
all tend to share similar foundations and concepts.

User Created Core Content
~~~~~~~~~~~~~~~~~~~~~~~~~

Whether you look at `Instagram`_, `Reddit`_ or `Stackoverflow`_ you'll see that users
are creating the core content. I define core-content as the content that everything
else flows from. With `Instagram`_ that content is photos, with `Stackoverflow`_
it's questions, they lead to likes, comments or answers, which builds the entire
community.

On some sites, like `Slate`_, or `Buzzfeed`_ or even more traditional media outlets,
the core content is created by journalists, but if we step back and just consider
a journalist a special-class of user who has rights to create this core-content, then
even more traditional media sites start taking on the same shape as a social-site.

To help content discovery, the core-content is often categorized into fixed categories
and/or tagged with dynamic tags. So your site might have fixed categories like `Tech`
and `Politics` to allow a sane organisation to your home-page, but content within
those categories might be tagged with more unique keywords like `Hillary` or `Hubble`
which would allow users to easily find similar content.

User Comments and Feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~

Perhaps the most important aspect, maybe even greater then the core-content
is the ability of users to comment on, or in some way provide feedback to
that core-content. Sometimes this is as simple as a 'like' button ala
`Facebook`_ other-times it's a up or down-vote ranking system like `Reddit`_
or `Stackoverflow`_. Generally those voting systems work alongside a
commenting system, normally allowing just pure text.

User to User Interaction
~~~~~~~~~~~~~~~~~~~~~~~~

Building relationships is one of the key goals of a social site. If you
enjoy the content of another user, you should be allow to follow them, allowing
you to be alerted whenever they contribute to the site.

In addition, direct communication between users is often implemented to allow
a more private communication channel that isn't covered by commenting on
core-content.

Housekeeping
~~~~~~~~~~~~

Users need to be able to register, request password resets and sign in and out.
Site's without decent administrative tools can quickly turn poisonous— it's
important for tools to allow troubled users to be banned or timed-out and for
content, be it core or commentary, to be removed if required.

Shared Foundations
~~~~~~~~~~~~~~~~~~

Most sites you'll visit will fit into the rough shape described above.
Check out a few of your favourite sites and see if they fit into this same concept, see if
they share the same foundations.

In this series, I'll detail my journey to build a web application that implements these
foundational ideas using the Flask framework and an assortment of extensions and packages
to make our progress a little smoother.

By the end you will be well placed to extend the project with your own ideas that give
your application the uniqueness that makes it stand out.
As you should be able to see, there's nothing particularly special
about a social site, so the shape of your own application can be wide and varied
while still building on this common core.

It's important to state that, this guide is *not* the one-true guide on how to approach
and complete a project. While the `Zen of Python`_ says:


    "There should be one— and preferably only one —obvious way to do it."

    -- Zen of Python


That's not true, at all. The beauty of Flask (and other micro-frameworks) are
that they provide you with perfectly formed lego blocks
with which to build your project— you can use those block to build anything
from a simple drafty shack to an ornate cathedral in a dozen of different ways.
If you prefer a more structured approach, frameworks like Django or Pyramid
provide a more concrete story for your project.

In the coming section, we'll go over what we want to build in a little more
detail, to define the scope of our project and give us something to work
towards.

Stay tuned.

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
.. _Facebook: http://www.facebook.com/