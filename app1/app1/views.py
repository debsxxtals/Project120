from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('landing_page')  # Redirect to landing page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def landing_page(request):
    return render(request, 'landing_page.html')

# app1/views.py or a separate encryption module

from cryptography.fernet import Fernet
from django.conf import settings

cipher = Fernet(settings.SECRET_KEY_APP)

def encrypt_message(message):
    """Encrypt the message using the stored key."""
    encrypted_message = cipher.encrypt(message.encode())  # Convert the string to bytes
    return encrypted_message

import requests

from django.shortcuts import render
from django.http import HttpResponse

def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            encrypted_message = encrypt_message(message)  # Encrypt the message

            # Send the encrypted message to App2's API endpoint via a POST request
            try:
                # Convert encrypted message to a proper format
                response = requests.post(
                    'http://127.0.0.1:8001/api/messages/',  # App2's endpoint URL
                    json={'message': encrypted_message.decode()}  # Send as JSON (not form-data)
                )

                if response.status_code == 200:
                    return HttpResponse("Message sent and encrypted successfully!")
                else:
                    return HttpResponse(f"Failed to send message: {response.status_code}")
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error: {e}")
    return render(request, 'send_message.html')
