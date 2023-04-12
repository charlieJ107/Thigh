# What Remains on Charlie

> A personal digital portfolio implement in Python Flask framework.

## Required Information

* Username/Student Number: C2xxxxxx
* OpenShift Deployed URL:
    * Staging Version: http://cxxxxxxx-cmt120-cw2-staging.apps.openshift.cs.cf.ac.uk/
    * Production Version: http://cxxxxx-cmt120-cw2.apps.openshift.cs.cf.ac.uk/

## Quick Start (Run Locally)

> Note: Although there's a `if __name__ == "__main__"` in script file, it will only start up a development server that
> only binding local loopback IP address for development purpose. Please use a production ready wsgi server to run the
> application.

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run with `flask`

You need to set your database connection string into the environment variable called `FLASK_SQLALCHEMY_DATABASE_URL` so
that could be detected and load by flask. As other configuration also loaded from environment variables only, you should
set them into environment variables with prefix `FLASK_` to provide your other custom config such as `FLASK_DEBUG` or
`FLASK_ENV`.

```bash
# Set database connection string
export FLASK_SQLALCHEMY_DATABASE_URL=sqllite://$(pwd)/project.db
# Run with python flask
python -m flask --app cmt120_cw2 run 
 ```

## Code Review Guidance

> Programs are meant to be ready by humans and only icidentally for computers to execute
>
> ——SICP, Harold Abelson and Gerald Jay Sussman

The entire project could be divided into 4 layers.

* View - containing templates in `template` folder
* Controller - Basic logic including handle requests and provide data to render template
* Service - The business logic that needs to invoke database operations such as ORM is encapsulated and provided to the
  controller for invocation.
* Data - Database access and Object mapping

```
├───database # Data layer including data model
├───service # Service layer
├───static # Static assets (view layer)
│   ├───css
│   ├───fonts
│   ├───img
│   └───js
├───templates # Templates files (View layer)
```

The entrance of the application is in `main.py`, which belongs to the **Controller** layer. Extension objects including
`db` object from `Flask_SQLAlchemy` are initialized in `extensions.py` independently to avoid circular import.

Methods in Services (defined in `service` folder) are called in different route function defined in `main.py`. These
service functions encapsulate the
business logic and data access process, return the very simple result to controller layer so that controller layer could
give the correct response directly without concerning the details about data managing.

Classes in `database` package containing the DB Model provided to the ORM to map the objects.

## External Library Licenses:

* [Bootstrap](https://getbootstrap.com/) - [MIT License](https://github.com/twbs/bootstrap/blob/main/LICENSE)
* [Flask](https://palletsprojects.com/p/flask/) - [BSD 3-Clause](https://github.com/pallets/flask/blob/main/LICENSE.rst)
* [Flask-SqlAlchemy](https://github.com/pallets-eco/flask-sqlalchemy/) - [BSD 3-Clause](https://github.com/pallets-eco/flask-sqlalchemy/blob/main/LICENSE.rst)

## References

* [Flask Documents](https://flask.palletsprojects.com/en/2.2.x/)
* [How To Add Authentication to Your App with Flask-Login | Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
* [How to Use One-to-Many Database Relationships with Flask-SQLAlchemy | Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy)
* [How To Use Many-to-Many Database Relationships with Flask-SQLAlchemy | Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy)
* [Werkzug document](https://werkzeug.palletsprojects.com/en/2.2.x/)
* [SQLAlchemy Documents](https://docs.sqlalchemy.org/en/14/)
* [Flask-SQLAlchemy documents](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)