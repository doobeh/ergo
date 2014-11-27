:title: Introduction
:date: 2014-11-27 18:00
:series: tellus
:tags: python, flask
:category: tellus
:slug: tellus-introduction
:authors: Anthony Plunkett
:summary: Introduction to a Flask development journal.

This journal is about development of a social site using the Flask framework.
This guide assumes a passing familiarity with Python
and Flask, but ideally should be helpful to newcomers to the Flask framework
that are looking to make the next step. If you think I can improve or expand
on anything to make it clearer— please do let me know.

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

The Project
-----------

I'm going to work towards building a site that clones the functionality
of `MetaFilter`_.  If the site is new to you, visit it, click around
and get a feel for it.

MetaFilter is a good goal because it's a relatively simple site graphically,
it doesn't make heavy use of jQuery, so lets us focus more on the Python
side of the equation and less on the interface.

The site is a good representation of a lot of popular web applications, it has:

-   **Users**— Who can sign in to access features and manage their account settings.
-   **Administrators**— A special class of user that can manage the site, removing posts, banning users, etc.
-   **Payment handling**— MetaFilter has a $5 joining fee to become a participating user.
-   **Posts/Questions and Comments**— Users can create posts and comment on other users content.
-   **Favourites/Flags**— Users have the ability to favourite posts, or flag them for administrative notice.
-   **Internal Messaging**— Users can privately message one another.
-   **Limits**— Users can only post one article a day, or ask one question a week.
    **Threads** are closed for more comments after set time periods.
-   **Tags**— Articles are categorized and tagged.
-   **Search**— The site can be searched.

Think of any web-application and you'll find it has most of those features,
so if you make it through this journal you should
have a really solid foundation for approaching projects of your own.

I tend to refer to this project as a journal, not a tutorial— I'm happy to
make mistakes and ponder other approaches, I think that's an accurate
reflection of real development.

Test Driven Design
------------------

One of my goals of this project is to use test-driven design (TDD) to help
shape the project, and set goals that take into account the end-users of
the site.

I like to think of TDD as story-telling.  We put ourselves into a users
shoes and then walk through the site, at each step of the journey we
test to see if that step was successful.

For example, a simple story for a user might be "Jane wants to log in
to the site to change her occupation" so lets break that down:

#. Jane goes to the homepage of our site
#. She clicks on the login button
#. She enters her username and password, and click the 'Sign In' button.
#. The site logs her in and returns her to the homepage.
#. She clicks on her name that is now shown on the navigation bar and chooses 'Manage' from the drop-down menu.
#. She edits her occupation in her user details and clicks 'Save'
#. The site returns her to the accout management page and tells her 'Profile Updated!'
#. She clicks on her name from the navigation bar, and chooses 'Sign Out'
#. She is logged out and returned to the homepage.

We *could* keep that story in our heads and as we developed and
we *could* occasionally run through that process to see if everything works,
that's level one. But better yet, we're developers, we can automate it!
We'll create some code that represents that story,
and then we can just run the test each
time we add some code.
When the test completes successfully, we know that that story
is complete.
By building up many stories that cover the gamut of your
users interactions on your site, we can use these tests to tell
us when our site is functionally complete.

For many new developers, it sounds slow, but as you get more experienced
you'll find that spending the time upfront to build these TDD stories
lets you get a more complete picture of what you're developing and
you will find that you end up saving a great deal of time.  This is
especially true if you're like me— a developer that tends to keep
adding features and tweaks to their projects and never actually get
them complete.

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. _MetaFilter: https://www.metafilter.com/