from cryptography.fernet import Fernet

# Generate a random key
key = Fernet.generate_key()

# Print the key to the console
print(key)
