# The Eye
Consumer Affairs Practical Test: https://gist.github.com/wsantos/fdc18cec2329777f74f1ba00098c9d0b

## About the models

I have created 3 models, Application, Session, and Event.

The model Application allows a Host to send data. In this model, you must add a name and a host using the admin (http://localhost:8000/admin/).

The model Session, only have the ID and the created_at field. This field is used only to log.

In the model Event I added the extra fields created_at and updated_at to allow the team finds errors like an event that has an invalid timestamp.

## About the API

I have created the API using Django Rest Framework, and the documentation is auto-generated using drf-yasg. After starting the project, you can see the documentation on http://localhost:8000/docs/.

## About the Celery

I'm using Celery to save all events to avoid blocking the requests. You need to install the Redis and start the celery process. See all the steps on [Start the project](#start-the-project).

## Observations

I'm using a class cache on EventView to avoid making many requests to verify if the host is allowed.

## Start the project

1. Clone repository
```shell
    git clone git@github.com:leonardocsantoss/the_eye.git
```

2. Create python 3 virtualenv
```shell
    python3 -m venv venv
```

3. Activate virtualenv
```shell
    . venv/bin/activate
```

4. Install libs
```shell
    pip install -r requirements.txt
```

5. Run migrate, to create a local database
```shell
    python manage.py migrate
```

6. Create a superuser
```shell
    python manage.py createsuperuser
```

7. Run test server
```shell
    python manage.py runserver
```
See the documentation on http://localhost:8000/docs/
And the admin on http://localhost:8000/admin/

- You need to create an Application using the admin to allow the Host to send data.


8. Install Redis using Docker
```shell
    docker run --name my-redis -p 6379:6379 -d redis
```

9. Run the Celery in another shell
```shell
    celery --app=the_eye worker
```