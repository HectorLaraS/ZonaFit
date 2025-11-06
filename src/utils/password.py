import hashlib

def hash_password_md5(password):
    """Hashes a password using MD5."""
    return hashlib.md5(password.encode()).hexdigest()