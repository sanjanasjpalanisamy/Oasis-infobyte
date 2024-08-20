import random
import string

def generate_password(length=12):
    # Define the characters that will be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password_length = 16  # You can change this to any length you prefer
print(f"Generated password: {generate_password(password_length)}")
