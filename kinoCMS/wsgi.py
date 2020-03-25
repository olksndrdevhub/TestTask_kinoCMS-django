"""
WSGI config for kinoCMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""


import os
import sys
sys.path.append('/home/ubuntu/django/kinoCMS/kinoCMS')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/ubuntu/django/kinoCMS/kinoCMS/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kinoCMS.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
