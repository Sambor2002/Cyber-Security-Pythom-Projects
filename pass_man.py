import hashlib
import getpass

password_menager={}

def create_account():
    username=input("Think of a username: ")
    password= getpass.getpass("And a password to match your account: ")
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    password_menager[username]=hashed_password
    print("Account created successfully!")

def login():
    username=input("Your username")
    password=getpass.getpass("Your password")
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    if username in password_menager.keys() and password_menager[username] == hashed_password:
        print("Logged in successfully!")
    else:
        print("Invalid credentials!")

def app():
    while True:
        choice=input("Enter 1 to create an account\nEnter 2 to login\nEnter 0 to exit: ")
        if choice=="1":
            create_account()
        elif choice=="2":
            login()
        elif choice=="0":
            break
        else:
            print("Invalid acction")

if __name__=="__main__":
    app()