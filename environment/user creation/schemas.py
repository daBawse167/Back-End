from models import duplicate_user, duplicate_email
import time

def signup():
    #sign up username
    username = input("Create a username: ")
    user_valid = duplicate_user(username)
    #check to see if the username is taken
    while user_valid=="invalid":
        username = input("Username taken. Please choose a different one: ")
        user_valid = duplicate_user(username)

    #sign up email
    email = input("Enter an email: ")
    email_valid = duplicate_email(email)
    #check to see if the email is taken
    while email_valid=="invalid":
        email = input("Email taken. Please choose a different one: ")
        email_valid = duplicate_email(email)

    password = input("Create your password: ")

    return [username, email, password]

def login():
    #stored emails
    #NEED TO CONNECT TO MONGODB
    emails = {"email":"password"}
    user_email = ""

    #ask user for email
    while True:
        input_email = input("Enter your email: ")
        if input_email not in emails.keys():
            print("email not found")
        else:
            user_email = input_email
            break

    #ask user for password after email has been entered
    while True:
        break_outer = False
        #gives the user 5 tries before locking out
        for i in range(5):
            password = input("Enter your password: ")
            #checks if password is correct
            if emails[user_email]==password:
                break_outer = True
                print("logging in")
                break
            else:
                print("password is incorrect")
        if break_outer == True:
            break
        #locks user out temporarily
        print("locking out for 5 seconds")
        time.sleep(5)