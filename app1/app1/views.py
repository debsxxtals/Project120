from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

import requests
from django.conf import settings

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

def decrypt_message(encrypted_message):
    """Decrypt the encrypted message using the stored key."""
    decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()  # Convert bytes to string
    return decrypted_message

import requests

from django.shortcuts import render
from django.http import HttpResponse


def send_message(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        bank_account = request.POST.get('bank_account')
        if amount and bank_account:
            # Encrypt both messages
            encrypted_amount = encrypt_message(amount)
            encrypted_bank_account = encrypt_message(bank_account)
            username = request.user.username

            try:
                response = requests.post(
                    'http://127.0.0.1:8001/api/messages/',  # App2's endpoint URL
                    json={
                        'username': username,
                        'amount': encrypted_amount.decode(),
                        'bank_account': encrypted_bank_account.decode()
                    }
                )

                if response.status_code == 200:
                    # Get the encrypted acknowledgment message from App2 
                    encrypted_acknowledgment_message = response.json().get('message') 
                    
                    # Decrypt the acknowledgment message 
                    acknowledgment_message = decrypt_message(encrypted_acknowledgment_message)
                    return render(request, 'send_message.html', {'acknowledgment_message': acknowledgment_message})
                else:
                    return HttpResponse(f"Failed to send message: {response.status_code}")
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error: {e}")

    return render(request, 'send_message.html')
