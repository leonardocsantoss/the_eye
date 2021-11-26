# The Eye
Consumer Affairs Practical Test: https://gist.github.com/wsantos/fdc18cec2329777f74f1ba00098c9d0b

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