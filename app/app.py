"""
This file exists for backward compatibility.
Use the main app.py or wsgi.py instead.
"""

from . import create_app

app = create_app()