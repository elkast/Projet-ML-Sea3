"""
WSGI entry point for production deployment.
Used with WSGI servers like Gunicorn or uWSGI.

Usage:
    gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
    gunicorn -w 4 -b 0.0.0.0:5000 --timeout 120 wsgi:app
"""

import os
from app import create_app

# Create application instance in production mode
app = create_app('production')

if __name__ == "__main__":
    # This is only for testing the WSGI app directly
    # In production, use a proper WSGI server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)