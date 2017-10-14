import unittest
from user import User
from credential import Credential

class TestUser(unittest.TestCase):
    '''
    class to test the functionality of user class
    '''
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.the_user=User('david','password')
        self.the_user1=User('njoroge','drowssap')

        # self.new_cred=('facebook','david@gmail.com','123qwerty',to_login)



    def tearDown(self):
        User.users_list=[]

    def test_init(self):
        '''
        test case to test if the object is initialized
        '''
        self.assertEqual(self.the_user.name,'david')
        self.assertEqual(self.the_user.password,'password')

    def test_register(self):
        '''
        test if the user is saved
        '''
        self.the_user.register()
        self.assertEqual(len(User.users_list),1)

    def test_login_checker(self):
        '''
        test if you can login you input the username and passord and returns true
        args:
            name: the username
        '''
        self.the_user.register()
        self.the_user1.register()

        to_login=User.login_checker('david','password')
        # self.assertTrue(to_login)
        self.assertEqual(to_login,self.the_user)

    def test_login(self):
        '''
        test case, given a username should more or less login--to be implemented--
        '''

    def test_display_all_users(self):
        '''
        test case that tests if users list is returned
        '''
        self.the_user.register()
        self.assertEqual(len(User.display_users()),1)

    def test_create_credentials(self):
        '''
        test case to create a credential within a user instance(account)
        '''
        self.the_user.register()
        self.the_user1.register()
        to_login=User.login_checker('david','password')
        self.new_cred=Credential('facebook','david@gmail.com','123qwerty',to_login)
        self.new_cred.save_credential()
        self.assertEqual(len(Credential.cred_list),1)

    def

if __name__=='__main__':
    unittest.main()
