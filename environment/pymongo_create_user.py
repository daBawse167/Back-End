import pymongo
import smtplib
from email.message import EmailMessage
import random
import string

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://tomH:mbWS0uIrROmONBOv@biodevice.3jz8qms.mongodb.net/")
db = client["your_database"]
collection = db["user_accounts"]

# Function to generate random verification code
def generate_verification_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Function to send verification email
def send_verification_email(email, code):
    msg = EmailMessage()
    msg.set_content(f"Your verification code is: {code}")
    msg['Subject'] = 'Account Verification Code'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.example.com', 587) as smtp:
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)

# Main function to create account
def create_account():                          #needs some requiredments for usersnames emails and passwords
    username = input("Enter username: ")
    email = input("Enter email address: ")     
    password = input("Enter password: ")

    #verification_code = generate_verification_code()
    #send_verification_email(email, verification_code)

    #user_input_code = input("Enter verification code sent to your email: ")

    #if user_input_code == verification_code:




    account = {                                     ##indent this out once / if we have a smtp server
        "username": username,
        "email": email,
        "password": password,
        "verified": False  # all account are currently unverifiable
    }   
    result = collection.insert_one(account)   
    
        
    #verification account was actually made

    # Check if insertion was successful
    if result.inserted_id:
        print("Account created successfully with ID:", result.inserted_id)
        return True
    else:
        print("Failed to create account.")
        return False     
    #    print("Account created successfully!")
    #else:
    #    print("Verification code does not match. Account creation failed.")



if __name__ == "__main__":
    create_account()