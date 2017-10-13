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
        
