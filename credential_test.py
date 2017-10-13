import unittest
from credential import Credential

class TestUser(unittest.TestCase):
    '''
    class to test the functionality of credential class
    '''
    def setUp(self):
        '''
        setup method to run before each test case
        '''
        self.new_cred=Credential('facebook','david@gmail.com','123qwerty')
        # self.the_user1=User('njoroge','drowssap')


    # def tearDown(self):
    #     User.users_list=[]
    #
    def test_init(self):
        '''
        test case to test if the credential is initialized
        '''
        self.assertEqual(self.new_cred.account,'facebook')
        self.assertEqual(self.new_cred.username,'david@gmail.com')
        self.assertEqual(self.new_cred.password,'123qwerty')

    # def test_register(self):
    #     '''
    #     test if the user is saved
    #     '''
    #     self.the_user.register()
    #     self.assertEqual(len(User.users_list),1)
    #
    # def test_login(self):
    #     '''
    #     test if you can login you input the username and passord and returns true
    #     args:
    #         name: the username
    #     '''
    #     self.the_user.register()
    #     self.the_user1.register()
    #
    #     to_login=User.login('david','password')
    #     self.assertTrue(to_login)
    #


if __name__=='__main__':
    unittest.main()
