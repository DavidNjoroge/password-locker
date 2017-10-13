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
    @classmethod
    def login( cls,name,password):
        '''
        method that checks if the user is already register and then login
        '''
        for user in User.users_list:
            if user.name==name and user.password==password:
                return True
            return False
