from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    users = User.objects.all()
    messages = Message.objects.all()
    return render(request, 'dashboard.html', {'users': users, 'messages': messages})

# app2/views.py or a separate decryption module

from cryptography.fernet import Fernet
from django.conf import settings

cipher = Fernet(settings.SECRET_KEY_APP)

def decrypt_message(encrypted_message):
    """Decrypt the encrypted message using the stored key."""
    decrypted_message = cipher.decrypt(encrypted_message).decode()  # Convert bytes back to string
    return decrypted_message


from .models import Message

def store_decrypted_message(sender, decrypted_message):
    message = Message(sender=sender, content=decrypted_message)
    message.save()


from rest_framework.views import APIView
from rest_framework.response import Response


# API View to handle incoming encrypted messages
class MessageReceiver(APIView):
    def post(self, request):
        encrypted_message = request.data.get('message')

        if not encrypted_message:
            return Response({'status': 'error', 'message': 'No message found in request'}, status=400)

        try:
            # Decrypt the message
            decrypted_message = decrypt_message(encrypted_message)  # No need to encode since it's already a string
            # Optionally store the decrypted message
            sender = request.user  # Assuming the message sender is the logged-in user
            Message.objects.create(sender=sender, content=decrypted_message)

            return Response({'status': 'success', 'message': 'Message received and decrypted!'}, status=200)

        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=400)





from django.shortcuts import render
from django.http import HttpResponse

def receive_message(request):
    if request.method == 'POST':
        encrypted_message = request.POST.get('encrypted_message')
        if encrypted_message:
            # Convert the encrypted message to bytes if necessary
            encrypted_message_bytes = encrypted_message.encode()

            decrypted_message = decrypt_message(encrypted_message_bytes)
            # Now process or store the decrypted message
            return HttpResponse(f"Decrypted message: {decrypted_message}")
    return render(request, 'app2/receive_message.html')
