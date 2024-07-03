import re

def validate_username(username):
    """Validate username: must be alphanumeric and 3-20 characters."""
    if not isinstance(username, str):
        return False
    return re.match(r'^[a-zA-Z0-9]{3,20}$', username) is not None

def validate_email(email):
    """Validate email format."""
    if not isinstance(email, str):
        return False
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validate_age(age):
    """Validate age: must be an integer between 0 and 120."""
    if not isinstance(age, int):
        return False
    return 0 <= age <= 120
