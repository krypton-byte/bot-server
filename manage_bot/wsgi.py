"""
WSGI config for manage_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see :)
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from socketio import Middleware
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application
from global_data.views import sio
import eventlet
import eventlet.wsgi
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manage_bot.settings')
django_app=StaticFilesHandler(get_wsgi_application())
application = Middleware(sio, django_app)
eventlet.wsgi.server(eventlet.listen(('0.0.0.0', int(os.environ.get("PORT",8000)))), application)

