
class Credential:

    """
    class that creates a new credential(cred)
    """
    cred_list=[]

    def __init__(self, account,username,password):
        '''
        define the properties of the class
        '''
        self.account=account
        self.username=username
        self.password=password

    def save_credential(self):
        '''
        method to save the credentials inputted
        '''
        Credential.cred_list.append(self)
