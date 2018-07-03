# lookup

lookup is a **simple** web application for searching and browsing mobile phone data, built with the [Django framework](https://www.djangoproject.com/).

Technologies used:

* [jQuery](http://jquery.com/) v3.1.2
* [jQuery UI](https://jqueryui.com/) v1.12.1
* [Animate.css](https://daneden.github.io/animate.css/) v3.6.1
* [Open Sans](https://fonts.google.com/specimen/Open+Sans?selection.family=Open+Sans) (GoogleAPIs)
* [fonoapi](https://fonoapi.freshpixl.com/)

 The program has a few `requirements.txt`, which are:

```
certifi==2018.4.16
chardet==3.0.4
Django==2.0.6
idna==2.7
pytz==2018.4
requests==2.19.1
urllib3==1.23
```

## Installation

### 1. virtualenv
Activate your [virtualenv](https://virtualenv.pypa.io/en/stable/installation/), and make an `env` with python3:

```
$ cd /path/to/your/envs
$ virtualenv -p python3 env
$ source env/bin/activate
```

### 2. Download
Grab a copy of the source code and clone it:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/kurtisauc3/zenpitwebapp.git
    $ cd zenpitwebapp

### 3. Requirements
 *requirements.txt* contains all the packages need to run the website. Make sure your env is activated and run:

`$ pip install -r requirements.txt`

### 4. Tweaks

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `webapp/settings.py`, find `SECRET_KEY` line, paste your secret key.

#### Initialize the database
Evem though this project doesn't use a database, you'll still have to migrate

`python manage.py migrate`

### Ready to Run

`python manage.py runserver`
