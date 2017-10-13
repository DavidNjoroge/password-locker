#!/usr/bin/env python3.6
from credential import Credential
from user import User

def register_user(name,password):
    '''
    Function that creates a new user
    '''
    new_user=User(name,password)

    return new_user
