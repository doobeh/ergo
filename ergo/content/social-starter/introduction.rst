:title: Introduction
:date: 2014-11-27 18:00
:series: starter
:series_index: 1
:tags: python, flask
:category: starter
:slug: starter-introduction
:authors: Anthony Plunkett
:summary: Beginners Guide to Building a Social Web Application.

This guide assumes you're a newcomer to Python and Flask.
If you think I can improve or expand on anything to make
it clearer— please do let me know.

This guide is *not* the one-true guide on how to approach and complete a project.
While the `Zen of Python`_ says:


    "There should be one— and preferably only one —obvious way to do it."

    -- Zen of Python


That's not true, at all, with micro-frameworks— the beauty of Flask is
that it provides you with perfectly formed lego blocks
with which to build your project— you can use those block to build anything
from a simple drafty shack to an ornate cathedral.  If you prefer a more
structured approach, frameworks like Django provide a more complete story
from which to build.

The Tellus Project
------------------

I'm going to work towards building a site that essentially clones the functionality
of `MetaFilter`_.  If the site is new to you, visit it, click around
and get a feel for it.  If you've used sites like StackOverflow or Quora, you'll
be generally familiar with the functionality I'm looking to build.

MetaFilter is a particularly good goal because it's a relatively simple site graphically,
it doesn't make heavy use of jQuery, so lets us focus more on the Python
side of the equation and less on the interface.

The site is a good representation of a lot of popular web applications, it has:

-   **Users**— Who can sign in to access features and manage their account settings.
-   **Administrators**— A special class of user that can manage the site, removing posts, banning users, etc.
-   **Payment handling**— MetaFilter has a $5 joining fee to become a participating user.
-   **Posts/Questions and Comments**— Users can create posts and comment on other users content.
-   **Favourites/Flags**— Users have the ability to favourite posts, or flag them for administrative notice.
-   **Internal Messaging**— Users can privately message one another.
-   **Limits**— Users can only post one article a day, or ask one question a week and threads
    are closed for more comments after set time periods.
-   **Tags**— Articles are categorized and tagged.
-   **Search**— The site can be searched.

Think of any web-application and you'll find it has most of those features,
so if you make it through this journal you should
have a really solid foundation for approaching projects of your own.

I tend to refer to this project as a journal, not a tutorial— I'm happy to
make mistakes and ponder other approaches, I think that's an accurate
reflection of real development.

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. _MetaFilter: https://www.metafilter.com/