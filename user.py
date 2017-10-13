# class for the user

class User:
    """
    class that creates a new user
    """
    users_list=[]

    def __init__(self, name,password):
        '''
        define the properties of the class
        '''
        self.name=name
        self.password=password
    def register(self):
        '''
        method that saves a new instance ie to register
        '''
        User.users_list.append(self)
