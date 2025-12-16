"""
Main application entry point for local development.
For production deployment, use wsgi.py or api/index.py (Vercel).
"""

from app import create_app
import os

# Create Flask application instance
# Use environment variable to determine config, default to development
config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    # Development server configuration
    import socket
    
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    
    # Get local IP for convenience
    local_ip = '127.0.0.1'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass
    
    print(f"\n{'='*60}")
    print(f"🚀 Flask Development Server Starting")
    print(f"{'='*60}")
    print(f"📍 Local:    http://localhost:{port}/")
    print(f"📍 Network:  http://{local_ip}:{port}/")
    print(f"⚙️  Config:   {config_name}")
    print(f"{'='*60}\n")
    
    # Run development server
    # For production, use: gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
    app.run(
        debug=(config_name == 'development'),
        host=host,
        port=port,
        use_reloader=True,
        threaded=True
    )