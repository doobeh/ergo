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


That's not true, at all. The beauty of Flask (and other micro-frameworks) are
that they provide you with perfectly formed lego blocks
with which to build your project— you can use those block to build anything
from a simple drafty shack to an ornate cathedral.  If you prefer a more
structured approach, frameworks like Django provide a more complete story
from which to build.

The Starter Project
-------------------

We're going to be working towards building a social site that allows users to post
new content and comment on those posts.  Think of a light version of Reddit, or Quora.

To get up and running quickly, we'll focus on the core functionality, then build outwards
to add some of the more fancy useful features in.
At the end of the project, we'll have a site that has the following features:

-   **Users**— Who can sign in to access features and manage their account settings.
-   **Administrators**— A special class of user that can manage the site, removing posts, banning users, etc.
-   **Posts/Questions and Comments**— Users can create posts and comment on other users content.
-   **Favourites/Flags**— Users have the ability to favourite posts, or flag them for administrative notice.
-   **Tags**— Articles are categorized and tagged.
-   **Search**— The site can be searched.

Think of any web-application and you'll find it has most of these features,
so if you make it through this guide, you'll have a solid foundation for
approaching projects of your own.

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. _MetaFilter: https://www.metafilter.com/