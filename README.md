# Group 1

# Django REST Framework Applications with Security Features

# Project Overview
This project demonstrates the use of Django REST Framework (DRF) to create two secure, inter-communicating applications, App1 and App2. The primary focus is on ensuring secure communication by encrypting and decrypting messages exchanged between the two applications using custom middleware. 

# Features
    Secure Communication:
        Messages sent between App1 and App2 are encrypted before transmission and decrypted upon receipt.
        Uses the cryptography library for encryption/decryption.
    
    Middleware Integration:
        Custom middleware ensures data is encrypted during API requests and responses.

# Core Functionality:
    App1:
        Users can register, log in, send messages to App2, and can received confirmation message from App2

    App2:
        Users can register, log in, view received messages, and send confirmation messages back to App1.

# Setup Instructions
    Prerequisites
        Python 3.9+
        Django 4.x
        Django REST Framework
        SQLite Viewer
        Django Cryptography
        Djangorestframework

# Installation
    Clone the repository:
        bash
        copy code
        git clone https://github.com/debsxxtals/Project120.git
        cd Poject120

    Set up a virtual environment:
        python -m venv venv
        venv\Scripts\activate

    Install dependencies if needed:

    Start the development servers:
        For App1:
        python manage.py runserver 8000

        For App2:
        python manage.py runserver 8001

# Future Enhancements
    Implement a real-time messaging system using WebSockets.

# Contributors
    Ria Mie Deborah Talaba
    Akima Arwen Leyson
    Albert John Agbo
    Eden Grace Moreno