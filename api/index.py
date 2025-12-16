"""
Vercel serverless function entry point.
This file is required for Vercel Python deployments.
"""

from app import create_app

# Create the Flask app instance
app = create_app('production')

# Vercel expects the app to be named 'app'
# This will be used as the WSGI application