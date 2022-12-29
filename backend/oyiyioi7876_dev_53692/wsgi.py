"""
WSGI config for oyiyioi7876_dev_53692 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oyiyioi7876_dev_53692.settings')

application = get_wsgi_application()
