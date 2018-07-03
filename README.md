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


    $ cd /path/to/your/envs
    $ virtualenv -p python3 env
    $ source env/bin/activate

If you don't have virtualenv, you will have to install it first. This can be easily done in your terminal:

    $ pip install virtualenv

*pip usually doesn't require `sudo`*
### 2. Download
Grab a copy of the source code and clone it:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/kurtisauc3/zenpitwebapp.git
    $ cd zenpitwebapp

### 3. Requirements
 *requirements.txt* contains all the packages need to run the website. Make sure your env is activated and run:

    $ pip install -r requirements.txt

### 4. Tweaks to files

#### SECRET_KEY

1. Open your `webapp/settings.py`, and find the `SECRET_KEY` line at the top.

2. Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, and copy it.

3. Paste your secret key over the text **your-secret-key-goes-here**:

        $ SECRET_KEY = "your-secret-key-goes-here"

#### Initialize the database
Even though this project doesn't use a database, you'll still have to migrate because Django requires this step to run.

    $ python manage.py migrate

### Ready to Run

    $ python manage.py runserver

See it in action at http://localhost:8000.
