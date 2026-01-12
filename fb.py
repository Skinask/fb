import itertools
import string
import time

def get_basic_info(username):
    # Simulated basic info retrieval
    # In real scenario, this would query a database or API
    users_db = {
        "alice": {
            "phone_numbers": ["1234567890", "0987654321"],
            "favorites": ["chocolate", "blue", "pizza"],
            "birthday": "19900115",
            "name": "alice"
        },
        "bob": {
            "phone_numbers": ["5551234567"],
            "favorites": ["soccer", "red", "burger"],
            "birthday": "19851230",
            "name": "bob"
        }
    }
    return users_db.get(username.lower(), None)

def generate_passwords(info):
    passwords = set()
    name = info["name"]
    birthday = info["birthday"]
    favorites = info["favorites"]
    phone_numbers = info["phone_numbers"]

    # Use birthday as is
    passwords.add(birthday)
    # Birthday with special chars
    for ch in ['!', '@', '#', '$', '%']:
        passwords.add(birthday + ch)
        passwords.add(ch + birthday)

    # Name with numbers and special chars
    for num in range(0, 100):
        passwords.add(f"{name}{num}")
        passwords.add(f"{num}{name}")
        for ch in ['!', '@', '#', '$', '%']:
            passwords.add(f"{name}{num}{ch}")
            passwords.add(f"{ch}{name}{num}")

    # Favorites combined with numbers and special chars
    for fav in favorites:
        for num in range(0, 100):
            passwords.add(f"{fav}{num}")
            passwords.add(f"{num}{fav}")
            for ch in ['!', '@', '#', '$', '%']:
                passwords.add(f"{fav}{num}{ch}")
                passwords.add(f"{ch}{fav}{num}")

    # Phone numbers as passwords and with special chars
    for phone in phone_numbers:
        passwords.add(phone)
        for ch in ['!', '@', '#', '$', '%']:
            passwords.add(phone + ch)
            passwords.add(ch + phone)

    return passwords

def brute_force_login(username):
    info = get_basic_info(username)
    if not info:
        print("User not found.")
        return

    print(f"Checking basic information for {username}...")
    print(f"Phone numbers: {info['phone_numbers']}")
    print(f"Favorites: {info['favorites']}")
    print(f"Birthday: {info['birthday']}")
    print("Starting password brute force...")

    passwords = generate_passwords(info)

    # Simulated correct password for demo
    correct_password = info["name"] + "42!"

    start_time = time.time()
    for pwd in passwords:
        # Simulate fast checking
        if pwd == correct_password:
            print(f"Password found: {pwd}")
            print(f"Login successful for user {username}")
            break
    else:
        print("Password not found in generated list.")
    end_time = time.time()
    print(f"Brute force took {end_time - start_time:.4f} seconds.")

def main():
    username = input("Put the username: ").strip()
    brute_force_login(username)

if __name__ == "__main__":
    main()
      
