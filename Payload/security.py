from cryptography.fernet import Fernet


def generate_key():
    """Generate a key for encryption and decryption."""
    return Fernet.generate_key()


def encrypt_message(message: str, key: bytes) -> str:
    """Encrypt a message."""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()


def decrypt_message(encrypted_message: str, key: bytes) -> str:
    """Decrypt a message."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()


def save_credentials_to_file(base_url: str, username: str, password: str, filename: str, key: bytes):
    """Save encrypted credentials to a file."""
    encrypted_base_url = encrypt_message(base_url, key)
    encrypted_username = encrypt_message(username, key)
    encrypted_password = encrypt_message(password, key)

    with open(filename, 'w') as file:
        file.write(f"Key: {key.decode()}\n")
        file.write(f"BaseURL: {encrypted_base_url}\n")
        file.write(f"Username: {encrypted_username}\n")
        file.write(f"Password: {encrypted_password}\n")


# Generate a key
key = generate_key()


def load_credentials_from_file(filename: str, key: bytes) -> tuple:
    """Load and decrypt credentials from a file."""
    with open(filename, 'r') as file:
        encrypted_base_url = file.readline().strip()
        encrypted_username = file.readline().strip()
        encrypted_password = file.readline().strip()

    base_url = decrypt_message(encrypted_base_url, key)
    username = decrypt_message(encrypted_username, key)
    password = decrypt_message(encrypted_password, key)

    return key, base_url, username, password