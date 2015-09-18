:title: The Project Scope
:date: 2015-09-17 19:55
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

Lets create four imaginary users and build a little story about each of them to
further define our site.

Content Creator Alice
~~~~~~~~~~~~~~~~~~~~~

**Alice**- is a first-time visitor to the site.  She visits our site and after
viewing the content, decides she wants to become a member and post an interesting
article she's found.  She clicks on the `Register` button and enters her desired
username, password and her active email address.  When she submit that form,
she gets told to check her email to activate her account.

She opens her mail-client and clicks the link in the new activation email in
her inbox, which takes her back to the site and she logs in successfully.

She clicks `Create Post` and enters the information for the article she wants
to share, she chooses to allocate it to the `Tech` section and she also
tags it `nuclear`, `breakthrough`.

When she's complete, she submits the form and is taken to her brand-new first
post on the site.  She's interested what other posts have been tagged with `nuclear`
so she clicks on the tag attached to her post and it takes her to a page
showing all the latest posts that have also been tagged `nuclear`.

Carol the Spammer
~~~~~~~~~~~~~~~~~

Carol signs up for an account and goes to the homepage and clicks on the post
by Alice-- she wants to badly promote her own site, so she just leaves a comment
saying "Hi check out my site! www.example.com". which has no relevance to Alice's
post.

Bob the Commenter
~~~~~~~~~~~~~~~~~

Bob logs into his account and clicks on the `Tech` category from the homepage
to see what's new.  He see's an interesting post by Alice and clicks on it.

He notices the first comment on the post is a spammy link, so he flags
it for attention to the site-admins.

After reading the article he adds a comment to the post, which includes
a link to a opinion piece that he found relevant to the topic at hand.

He also found the post so interesting that he's interested when Alice posts
anything else new, so he clicks on Alice's name to bring up her profile,
then chooses to follow her— later when she posts another article,
it'll show up on his recent follower activity.

Diane the Administrator
~~~~~~~~~~~~~~~~~~~~~~~

Diane signs into her administrative account and views her admin interface to
see the size and shape of the site.

She notices on her status page that a comment has been
flagged by several users and clicks to view it.
It's clearly a spam link, by Carol, a new user. Diane decides that this does
not bode well for Carol's future with the site, quickly deletes the comment and
bans Carol from future activity.

Diane read Alice's post while she was reviewing the comment, and really enjoyed
it.  She clicks the favourite button and also sends Alice a direct message
through the site saying 'Great first post! Welcome to the site!'.


Setting the Boundaries of our App
---------------------------------

In those four short stories, we've actually defined a lot of functionality
for our site, and we've got a feel for how a user would actually use it.
We now know that we need to have a mechanism to flag posts or comments
for administrative attention, as well as an administrative interface that
can report on those flags.

We know that tags link posts together, and clicking on one will take us
to similarly tagged posts.

We've also defined that users need to confirm their email addresses to
hopefully reduce the instances of user's like Carol.

Putting yourself into these types of stories can really help to solidify
what the flow of the site is.  We've only done a few quick stories to
illustrate the concept, but the more detailed you are with
you projects, the better you can define the edges of our application.

Now that we've got a rough shape to our application, we can start
building it.  The next section will briefly go over how to get you
computer into the right configuration so we're all starting off
from the same place.

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