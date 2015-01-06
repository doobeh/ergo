:title: SQLAlchemy Cheat Sheet
:date: 2015-01-05 20:26
:date: 2015-01-05 20:26
:tags: flask, python, jinja, sqlalchemy
:category: flask
:slug: sqlalchemy-cheatsheet
:authors: Anthony Plunkett
:summary: SQLAlchemy ORM Reference
:status: published

SQLAlchemy is largely magic, you ask it to do things, and it just works.
This is especially true when dealing with 'simple' relationships, e.g.
one `User` has many `Books`.

This article is going to be a quick overview of how to query a variety
of common relationships and will move on to the not so common versions.

We'll want to play with our code, so lets create a little application
for it— I tend to do mostly do web-development using Flask, and
so I tend to also use Flask-SQLAlchemy for my database work.  It's just
SQLAlchemy with a few utilities added into it— if you're a pure SQLAlchemy
user, you'll follow along just fine.

Here's our basic app:

.. code-block:: python

    from flask import Flask
    from flask.ext.sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    db = SQLAlchemy(app)

    ## SQLAlchemy Models will live here... So replace the below User model with the
    ## example if you wish to play with it.

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)

    ## Then we'll run in an app context to work with the ORM:

    with app.app_context():
        db.create_all()

        # Replace the below with the query examples to have a play around. e.g:

        u = User(name='Alice')
        db.session.add(u)
        db.session.commit()

        alice = User.query.filter_by(name='Alice').first()
        print alice

        # <User: Alice>


One `Author` has many `Books`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the most common relationship, a one-to-many relationship.  It's the building block
of all database schemas worthy of the name.  It's worth looking at relationships from both
sides to fully understand their scope and limitations.  Remember that *many* is a number from
zero upwards.

If I draw the relationship out I get::

    ----------           --------
    | AUTHOR |1---------M| BOOK |
    ----------           --------

If I stand inside the `Author` side of the relationship and look out towards the `Book`
object, I can see a `M`-- so I can say "I the author can write
none, one or several books."  If I then walk over to the `Book` side of the relationship
and look out towards the `Author` object, I just see a `1` which means I
can say "I, a book have a single author.  I cannot have several authors". If we
jump out of SQLAlchemy and look directly at the database tables, you'll see that in
a one-to-many relationship, the many side (our book table) would have a foreign-key
reference (in our case `author_id` within it) which is the structure of the relationship.

This makes sense— if you imagine picking a book up off a shelf in a library, it would
have a reference to the author, in the case of a physical book, the reference is actually
the authors name, but to find more about the author (to join to another source of data)
we would have to go to Wikipedia and use that reference to find out more information.

So in a one-to-many join, the reference that defines the relationship lives on the
many side.

.. code-block:: python

    class Author(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)
        articles = db.relationship('Book', backref='author')

        def __repr__(self):
            return '<Author:{}>'.format(self.name)


    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.Text)
        content = db.Column(db.Text)
        author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

        def __repr__(self):
            return '<Book:{}>'.format(self.title)


And now lets enter some data to play with:

.. code-block:: python

    bob = Author(name='Bob')
    dune = Book(title='Dune')
    moby_dick = Book(title='Moby Dick')

    carol = Author(name='Carol')
    ring_world = Book(title='Ring World')
    fahrenheit = Book(title='Fahrenheit 451')

    bob.books = [dune, moby_dick]
    carol.books = [ring_world, fahrenheit]

    db.session.add(bob)
    db.session.add(carol)
    db.session.commit()

And finally, the fun step— querying the models and relations.

.. code-block:: python

    author = Author.query.filter_by(name='Carol').first()
    print author  # <Author:Carol>
    print author.books  # [<Book:Ring World>, <Book:Fahrenheit 451>]

    dune_book = Book.query.filter_by(title='Dune').first()
    print dune_book  # <Book:Dune>
    print dune_book.author  # <Author:Bob>


So we can see how to query from either the `Book` side or the `Author` side of the relation.

Many to Many (M2M) Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a Many to Many relationship both sides of the relationship can have zero to many entries,
we are going to extend our example to include a M2M relationship by modelling the idea that
"many `Books` have many `Categories`".  To be clear, I mean that a book might be both in
Romance *and* Comedy, or Science Fiction *and* Fantasy.

At first glance this feels the same as the one-to-many relationship we worked on before
(one Author has many Books) but in that case, one book could only have one author.  In a M2M
relationship we're saying one Book has many categories, but we're also saying that one category
has many books.

When we spoke about one-to-many relations, we said that the reference that defines
the relationship lives on the many side— but now we have two many sides
(which is.. too many) and it simply won't work.

A M2M relationship is actually just two one-to-many relationships working together.  We might
initially think a M2M relationship looks like this::

    --------              ------------
    | Book |M------------M| Category |
    --------              ------------

The problem with that is that because both sides need to hold multiple references to the other
table, there's nowhere to store those references, while retaining the benefits of using
a database.  So what a M2M relationship actually looks like is::

    --------     -----------------     ------------
    | Book |1---M| book_category |M---1| Category |
    --------     -----------------     ------------

In SQLAlchemy parlance it's referred to as an association table.  It's job is
to manage the associations between the `Book` and `Category` tables.  If we
delved into the `book_category` table we would see just two columns: `book_id`
and `category_id` (remember, the 'many' side of a relation gets the foreign-key
references).

Because this is a very common database pattern, SQLAlchemy uses some magic that
allows us to talk directly between `Book` and `Category` objects, under the
surface SQLAlchemy will manage that `book_category` table for us.

Sometimes you wish to hold some information within that association table, perhaps if you
had a M2M relationship between student and exams, you might want to include their grade or
date they took the exam
in the association table, in that case you want SQLAlchemy to define it as an association
*object* and *not* a association table.  In short, association tables are transparent
to you, whereas association objects have data of their own which you access.

For now, we'll build an association table, as we're not storing extra data within it and
are only concerned about the `Book` and `Category` endpoints.  Lets add that table and
the `Category` object to live along side the models we've already created:

.. code-block:: python

    categories = db.Table('categories',
        db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
        db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
    )

    class Category(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)
        books = db.relationship('Book', secondary=categories,
                                backref=db.backref('categories', lazy='dynamic'))
        def __repr__(self):
            return '<Category:{}>'.format(self.name)


Now lets add some data, assign the books we have already created to those categories
and show how the relationship works both ways.

.. code-block:: python

    scifi = Category(name='Science Fiction')
    classic = Category(name='Classic')

    classic.books = [moby_dick, dune, fahrenheit]
    scifi.books = [dune, ring_world]

    db.session.add_all([classic, scifi])
    db.session.commit()

    print dune, dune.categories.all()
    # <Book:Dune> [<Category:Classic>, <Category:Science Fiction>]

The reason we added a `.all()` to the categories is that
we defined the categories/book relationship as dynamic.  That means it returns
a query object, we need to launch that query to get results, `.all()` is one of
the triggers to do that.  The big benefit of defining the relationship as dynamic
is that we can run further filters and queries on it:

.. code-block:: python

    print dune.categories.filter(Category.name.ilike('sci%')).all()
    # [<Category:Science Fiction>]

In that example we've further filtered down results to those that
have a name starting with 'sci' the `i` in `ilike` indicates that it's
a case-insensitive search.

That's not the best example, so lets do something a little more useful.

Querying Over Multiple Relations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now have an author who was written many books each of which can belong to multiple
categories.  We have one relationship tying the `Author` to the `Book` class, and another
tying the `Book` to the `Category` class.

We've shown how we can use those relationships individually, but lets go one step
further and talk across both.  How would we find out which authors have penned
a science fiction book?  We'll add a third author, Alice, who has only written
classics to show it's working:

.. code-block:: python

    alice = Author(name='Alice')
    beowulf = Book(title='Beowulf')
    beowulf.author = alice
    beowulf.categories = [classic]
    db.session.add(beowulf)
    db.session.commit()

    print Author.query.join(Author.books).filter(
        Book.categories.contains(scifi)).all()

    # [<Author:Carol>, <Author:Bob>]

It's very readable, we ask for the Author objects, and tell it to join to the
author's books— then we use the relationship between books and categories to
filter to those which contain Science Fiction.

Next lets approach from the opposite side, we want to find out which categories
Carol has published within.  We're no longer able to use the 'contains' method because
we're querying from the many to one side of the relationship between `Book` and `Author`.

To put it another way, the `contains` clause would essentially ask
"Out of the list of authors on this book, is one of them Carol?" which would raise
an error, because `contains` is expecting a list and would only get a single value
(what we refer to as a scalar) because we've defined 'A `Book` can only have a single
`Author`' when we built our relationship.

Because we're dealing with a scalar value on Author,
we could just use a simple `==` comparison:

.. code-block:: python

    print Category.query.join(Category.books).filter(
        Book.author==carol).all()

    # [<Category:Classic>, <Category:Science Fiction>]


Here is the complete code for you to run and experiment with:

[gist:id=574fc95caee4c22f21ed]