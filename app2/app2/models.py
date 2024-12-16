# app2/models.py

from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=150)  # Store username
    amount = models.TextField()  # Decrypted amount
    bank_account = models.TextField(null=True, blank=True)
  # Decrypted bank account
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} withdraws {self.amount} at {self.timestamp} /n Bank Account: {self.bank_account}"
