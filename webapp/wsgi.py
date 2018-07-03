"""
That app variable down there does the heavy lifting for how this beauty works as a web app
Web apps like to talk, you know?
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

# this one :)
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
