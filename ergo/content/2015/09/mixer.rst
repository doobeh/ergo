:title: Simple SQLAlchemy Flask Fake Data with Mixer
:date: 2015-09-08 22:23
:tags: flask, mixer, sqlalchemy, fixtures
:category: flask
:slug: simple-data-generator-for-flask-sqlalchemy
:authors: Anthony Plunkett
:summary: Easy SQLAlchemy fixtures in Flask with Mixer
:status: published

Once you have your data-model built for your application, you need to load it
with data so you can fully explore it.  You can't start to really build a
solid user-interface, be it web, app or desktop until you have data that
represents what the real end user will experience.

`Mixer`_ is a smart and easy solution to that problem.  We'll walk through
a simple example to show how you might go about loading your Flask application
with a few thousand elements of data.

Lets build a straightforward application that has `Users`, `Posts` and `Comments`
and manually set up a `User`, `Post` and `Comment`.

.. code-block:: python

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.secret_key = 'MixerTest'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'

    db = SQLAlchemy(app)


    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer(), primary_key=True)
        username = db.Column(db.String(20), nullable=False)
        email = db.Column(db.String(50), nullable=False)


    class Post(db.Model):
        __tablename___ = 'post'
        id = db.Column(db.Integer(), primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
        user = db.relationship('User', backref='posts')


    class Comment(db.Model):
        __tablename__ = 'comment'
        id = db.Column(db.Integer(), primary_key=True)
        content = db.Column(db.Text(), nullable=False)
        user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
        user = db.relationship('User', backref='comments')
        post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
        post = db.relationship('Post', backref='comments')

    with app.app_context():
        db.create_all()

        new_user = User(username='alice', email='alice@example.com')
        new_post = Post(title='Check out this gif!', user=new_user)
        new_comment = Comment(content='LOL! YOLO!', post=new_post, user=new_user)
        db.session.add(new_user)
        db.session.commit()

        c = Comment.query.first()
        print(c.content)  # LOL! YOLO!
        print(c.user.username) # alice
        print(c.post.title) # Check out this gif!


We've defined a `User` who can create many `Post` objects and many `Comment` objects, each `Comment`
belongs to a `Post` and a `User`.  At this stage in your app, you'd want to load several users,
dozens of Posts and perhaps hundreds of comments.  This is where `Mixer`_ can swoop in
and help us out.

One note, the `nullable=False` is important, it's telling our database that we *need* data for that
entry, and we'll complain if we don't get it.  If Mixer looks at a column where `nullable=True`
(which is the default behaviour) then it will say "Pfft, I won't bother making data for that column
because it's optional".

Lets begin by installing it via `pip install mixer` and then use it to build:

-   10 `Users`
-   100 Posts (Each linked to a `User`)
-   1000 Comments (Each linked to a `User` and `Post`)

Sounds tricky, but we can do it in six lines of code.  Lets just add the
following code below to our program:

.. code-block:: python

    from mixer.backend.flask import mixer
    mixer.init_app(app)

    users = mixer.cycle(10).blend(User)
    posts = mixer.cycle(100).blend(Post, user=mixer.SELECT)
    comments = mixer.cycle(1000).blend(Comment, user=mixer.SELECT, post=mixer.SELECT)


That's it!  Lets grab the 500th `Comment`  and look into it's details:

.. code-block:: python

    c = Comment.query.get(500)

    print("Content:", c.content)
    # Content: Et debitis alias sint dicta. Asperiores ...

    print("Post Title:", c.post.title)
    # Post Title: Debitis Et Velit Suscipit Ullam Voluptatibus

    print("Username:", c.user.username, "Email:",  c.user.email)
    # Username: parkpotato9 Email: bloodcrunching1@microsoft.tm


Notice how Mixer was smart enough to infer our `email` field needed a fake email,
our `username` needed a believable username and even that our `title` would
need Title Casing.

Because we have the relationships built, we could have asked Mixer to
do all three steps by itself by just asking `comments = mixer.cycle(100).blend(Comment)`
but we would have ended up with 200 `User` objects and 200 `Post` objects because it wouldn't
have known to randomly select an existing entry from the database and so would
have created a new `User` for each `Comment`.

Full working example can be found below:

[gist:id=6b375b107704da4030f7]

.. _Mixer: https://mixer.readthedocs.org/en/latest/
