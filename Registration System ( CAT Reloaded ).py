import hashlib

users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    print("- Register")
    
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    
    if email in users_db:
        print("Email already exists! Please log in instead.")
        return
    
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    
    users_db[email] = {
        'username': username,
        'password': hashed_password
    }
    
    print(f"Registration successful! You can now log in with your email {email}.\n")

def login():
    print("- Login")
    
    email = input("Enter your email: ")
    
    if email not in users_db:
        print("Email not found. Please register first.")
        return
    
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    
    if users_db[email]['password'] == hashed_password:
        print(f"Login successful! Welcome {users_db[email]['username']}.\n")
    else:
        print("Incorrect password. Please try again.\n")

def main():
    while True:
        print("- Welcome,CAT Reloaded Team, Here is my registration and authentication system!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
