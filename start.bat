@echo off
echo ========================================
echo  Flask ML Application - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Check if .env exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Creating .env from .env.example...
    if exist ".env.example" (
        copy .env.example .env
        echo Please edit .env file with your configuration
        echo.
    ) else (
        echo .env.example not found. Please create .env manually.
        echo.
    )
)

REM Create necessary directories
if not exist "uploads\" mkdir uploads
if not exist "logs\" mkdir logs
echo.

REM Start the application
echo Starting Flask application...
echo.
python app.py

pause