def password_generator(length: int):
    """
    Generates a random password of specified length.
    """
    import random 
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return f"Generated password: {password}"