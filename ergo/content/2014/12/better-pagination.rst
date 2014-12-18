:title: Better Pagination
:date: 2014-12-17 13:26
:modified: 2014-12-17 13:26
:tags: flask, python, jinja
:category: flask
:slug: better-pagination
:authors: Anthony Plunkett
:summary: Using macros to deploy pagination quicker
:status: published

.. highlight:: python

After starting a new project that involved long lists of products,
I inevitable turned to pagination to help manage the user interface
and then I was reminded about how much boilerplate code is required
on each template to get it working.

The Flask-SQLAlchemy includes a helpful pagination class utility
that integrates easily into a standard ORM query— here's a simple
example:

.. code-block:: python

    @app.route('/shop/department/<name>/')
    @app.route('/shop/department/<name>/pg<int:page>')
    def department(name, page=1):
        dept = Department.query.filter_by(slug=name).first_or_404()
        products = Product.query.filter_by(department=dept).paginate(
            page, app.config["PRODUCTS_PER_PAGE"]
        )

        return render_template(
            'department.html', department=dept, products=products
        )

This is an example taken from a straightforward shopping application,
it finds out what department the user is looking at, then returns
the products within that department as a pagination object.

In your Jinja template, you then access the properties of the pagination
object to build your user interface.  Normally that looks something like:

.. code-block:: python

    {# Display product data #}
    {% for product in products.items %}
        <p>{{ product.description }}</p>
    {% endfor %}

    {# If we have previous posts #}
    {% if products.has_prev %}
        <a href="{{ url_for('department', slug=department.slug, page=products.prev_num) }}">
            &laquo; Previous products
        </a>
    {% else %}
        &laquo; Previous products
    {% endif %}
    |
    {% if products.has_next %}
        <a href="{{ url_for('department', slug=department.slug, page=products.next_num) }}">
            Next products &raquo;</a>
    {% else %}
            Next products &raquo;
    {% endif %}

The downside of that is it's a lot of boilerplate code to use on each template.
Your endpoints and arguments for your `url_for` is going to change on each
view, so it forces the front-end designer to keep copy and editing this type
of layout.

A Better Way™
-------------

Instead, we can lean on the information we already have to make some intelligent
choices on how we wish to generate our pagination.  Here is our macro that will
handle it generically:

.. code-block:: jinja

    {% macro paginate(paginator) %}
        {# A generally pluggable pagination macro, just supply it with the pagination object #}
        {# formatted for Bootstrap 3 #}

        {% set view_args = request.view_args %}
        {% do view_args.pop('page') %}

        <div class="text-center">
            <ul class="pagination pagination-lg">

                {% if paginator.has_prev %}
                    <li class="active">
                        <a href="{{ url_for(request.endpoint, page=paginator.prev_num, **view_args) }}">&laquo;</a>
                    </li>
                {% else %}
                      <li class="disabled"><a href="#">«</a></li>
                {% endif %}

                {% if paginator.has_next %}
                    <li><a href="{{ url_for(request.endpoint, page=paginator.next_num, **view_args) }}">&raquo;</a></li>
                {% else %}
                    <li class="disabled"><a href="#">&raquo;</a></li>
                {% endif %}
            </ul>
        </div>
    {% endmacro %}

Now when you want pagination in your template, just do the following (assuming the above
code is saved in a file called '_helpers.html':

.. code-block:: jinja

    import '_helpers.html' as helpers

    {% for product in product.items %}
        <p>{{ product.description</p>
    {% endfor %}

    {{ helpers.paginate(products) }}

And it's good.  The important thing is does is to grab the current endpoint that is being
accessed from `request.endpoint` and then the arguments that were used to generate the
url from `request.view_args`.  That `view_args` dictionary is going to include a page
key, which we don't want since we'll be adding one in, so we `pop` it off the list using
the `do` function.

The `do` function is part of a built-in, but not enabled Jinja extension, it executes
the commands without doing printing out any returned values.  You'll need to
register it against your Flask application by doing the following:

.. code-block:: python

    app.jinja_env.add_extension('jinja2.ext.do')

Now we have the `endpoint`, and the cleaned `view_args` which we can use in tandem with
the pagination object to generate our pagination url's:

.. code-block:: jinja

    {{ url_for(request.endpoint, page=paginator.next_num, **view_args) }}

Which all means we get all of that boilerplate generated for us automatically without
having to worry about remembering endpoints and their associated arguments.

