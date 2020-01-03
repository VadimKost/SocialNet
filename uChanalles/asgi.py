"""
ASGI config for uChanalles project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import django
from channels.routing import get_default_application
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uChanalles.settings")
django.setup()
application = get_default_application()