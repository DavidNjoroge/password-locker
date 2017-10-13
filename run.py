#!/usr/bin/env python3.6
from credential import Credential
from user import User

def register_user(name,password):
    '''
    Function that creates a new user
    '''
    new_user=User(name,password)

    return new_user
def save_users(user):
    '''
    function that saves a new user
    '''
    user.register()
def login_user(name,password):
    '''
    function to login
    '''
    loggedin=User.login_checker(name,password)
    return loggedin

def display_users():
    '''
    function that returns all the saved users
    '''
    return User.display_users()

def main():
    print('Hello! welcome to our password locker')
    while True:
        print('if you would like to register, use short code "reg" or if login use "log" ')
        short_code=input().lower()
        if short_code=='reg':
            print('enter your new username')
            user_name=input()
            print('enter your new password')
            user_password=input()
            save_users(register_user(user_name,user_password))
            print('new user created')
        elif short_code=='show':
            if display_users():
                print('here is a list of all users')

                for user in display_users():
                    print('the users are '+f"{user.name}")
            else:
                print('\n')
                print('you dont have any users')

        elif short_code=='log':
            print('enter your username')
            user_name=input()
            print('enter your password')
            user_password=input()
            respnse=login_user(user_name,user_password)
            print(respnse)
            if respnse==None:
                print('wrong username or password')
            else:
                print('you are logged in')
                print('\n')
                while True:
                    print('use shortcode "nc" for new credential "sc" to show credentials')
                    short_code = input().lower()
                    if short_code=='nc':
                        short_code = input().lower()
                        print("New credential")
                        print("-"*10)
                        print ("Account ....")
                        account = input()

                        print ("username ....")
                        user_name = input()

                        print ("password ....")
                        password = input()








if __name__ == '__main__':

    main()
