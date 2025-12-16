"""
Setup script for the Flask ML application.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="projet-ml-sea3",
    version="0.1.0",
    author="Sossou Melchisedek",
    author_email="orsinimelchisedek@gmail.com",
    description="Application Flask pour l'analyse de données et prévisions ML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Projet-ML-SEA3",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "flask-ml-app=app:create_app",
        ],
    },
    include_package_data=True,
    package_data={
        "app": [
            "static/**/*",
            "templates/**/*",
        ],
    },
)