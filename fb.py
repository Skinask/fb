# Facebook Cloning Random Command

import random
import string

def generate_random_credentials():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    return username, password

def login_to_facebook(username, password):
    # Simulate login process (this is a placeholder)
    success = random.choice([True, False])
    return success

def main():
    while True:
        username, password = generate_random_credentials()
        if login_to_facebook(username, password):
            print(f"Successful login with Username: {username} and Password: {password}")
            break

if __name__ == "__main__":
    main()
    
