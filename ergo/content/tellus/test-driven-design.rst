:title: Test Driven Design
:date: 2014-11-28 20:46
:series: tellus
:series_index: 4
:tags: python, flask
:category: tellus
:slug: tellus-tdd
:authors: Anthony Plunkett
:summary: Test Driven Design


One of my goals of this project is to use test-driven design (TDD) to help
shape the project, and set goals that take into account the end-users of
the site.

I like to think of TDD as story-telling.  We put ourselves into a users
shoes and then walk through the site, at each step of the journey we
test to see if that step was successful.

A simple story for a user could be "Alice wants to log in
to the site to update the occupation on her profile
page" so lets break that down:

#. Alice goes to the homepage of our site
#. She clicks on the 'Sign In' link.
#. She enters her username and password, and submits the form.
#. The site logs her in and returns her to the homepage.
#. She clicks on her name that is now shown on the navigation bar and chooses 'Manage' from the drop-down menu.
#. She edits her occupation in her user details and clicks 'Save'
#. The site returns her to the account management page and tells her 'Profile Updated!'
#. She clicks on her name from the navigation bar, and chooses 'Sign Out'
#. She is logged out and returned to the homepage.

We *could* keep that story in our heads and as we developed and
we *could* occasionally run through that process to see if everything works,
but after the fifteenth time, you'd start getting bored, and you'd stop
doing it.  We can do better.  Let's give the boring task of running these
stories to the computer.

So, we'll create some code that represents that story,
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
you will find that you end up saving a great deal of time.

Here's a rough example of the first few parts of the story.  Don't try
and run it just yet, this is just the code that handles our story, there's
more code required to get the test suite running with our application.

.. code-block:: python

        def test_profile_update(self):
            # Alice goes to the homepage of our site:
            self.browser.get(app.config["SITE_URL"])
            self.assertIn('REF:HOME', self.browser.page_source)

            # She clicks on the 'Sign In' link:
            self.browser.find_element_by_id('signin').click()
            self.assertIn('REF:SIGNIN', self.browser.page_source)

            # She enters her username and password, and submits the form.:
            self.browser.find_element_by_id('email').send_keys('email@example.com')
            self.browser.find_element_by_id('password').send_keys('password')
            self.browser.find_element_by_id('submit').click()

            # The site logs her in and returns her to the homepage.
            self.assertIn('REF:HOME', self.browser.page_source)
            self.assertIn('Alice', self.browser.page_source)

            # Etc.

