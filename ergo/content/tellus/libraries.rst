:title: Libraries
:date: 2014-11-28 19:00
:series: tellus
:series_index: 3
:tags: python, flask
:category: tellus
:slug: tellus-libraries
:authors: Anthony Plunkett
:summary: Helpful Libraries
:status: draft

In addition to the Flask extensions we briefly went over, we're going to lean
on some other great libraries to make our life even easier.

Selenium
--------

We've talked about TDD and the testing stories-- these kinds of tests are called
functional tests, and if you were to carry them out manually, you would launch
a web-browser, navigate to the site and step through the guide.

We want to automate that, so we need to get the computer to handle that browser
session, click on the right links-- `Selenium`_ lets us do that.

Selenium automates web-browsers.  You can tell it to open up Firefox, navigate
to Google and run a search, and it'll do it exactly how a human user would.
We're going to feed it our stories and ask it to run them for us, and we'll
sit back and get the results when it's finished.


Stripe
------

`Stripe`_ is a nice, secure and modern payment gateway service.  They'll handle
credit-card payments for our project, and give us a nice `Python API`_ to send
charges and optionally set up subscription payments.  The big advantage of
Stripe is that you *never* see the credit-card information, their javascript
library `Stripe.js`_ converts the card-data into a single-use token, which
means you can never screw up and leak your customers card data.

.. code-block:: python

    import stripe
    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

    try:
        stripe.Charge.create(
          amount=400,
          currency="usd",
          card="tok_153kit2eZvKYlo2Cj8RCT4yi", # obtained with Stripe.js
          description="Charge for test@example.com"
        )
        print 'Woo, Card Charged!'

    except stripe.error.CardError, e:
        print 'Boo.. Payment failed :('

.. _Stripe.js: https://stripe.com/docs/stripe.js
.. _Stripe: https://stripe.com
.. _Python API: https://stripe.com/docs/api/python
.. _Selenium: http://www.seleniumhq.org/