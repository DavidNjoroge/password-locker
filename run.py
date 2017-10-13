#!/usr/bin/env python3.6
from credential import Credential
from user import User

def register_user(name,password):
    '''
    Function that creates a new user
    '''
    new_user=User(name,password)

    return new_user
def login_user(name,password):
    '''
    function to login
    '''
    new_user.User.login_user()

def create_credential(account,username,password):
    '''
    function that creates a new credential
    '''
    new_cred=Credential.save_credential(account,username,password)
    return new_cred
