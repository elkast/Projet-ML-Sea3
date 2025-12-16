#!/bin/bash

echo "========================================"
echo " Flask ML Application - Quick Start"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "WARNING: .env file not found!"
    if [ -f ".env.example" ]; then
        echo "Creating .env from .env.example..."
        cp .env.example .env
        echo "Please edit .env file with your configuration"
        echo ""
    else
        echo ".env.example not found. Please create .env manually."
        echo ""
    fi
fi

# Create necessary directories
mkdir -p uploads logs
echo ""

# Start the application
echo "Starting Flask application..."
echo ""
python app.py