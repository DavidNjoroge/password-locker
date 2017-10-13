import unittest
from user import User

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

    def test_login(self):
        '''
        test if you can login you input the username and passord and returns true
        args:
            name: the username
        '''
        self.the_user.register()
        self.the_user1.register()

        to_login=User.login('david','password')
        self.assertTrue(to_login)



if __name__=='__main__':
    unittest.main()
