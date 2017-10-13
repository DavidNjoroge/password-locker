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
        self.the_user=User('David','password')

    def test_init(self):
        '''
        test case to test if the object is initialized
        '''
        self.assertEqual(self.the_user.name,'David')
        self.assertEqual(self.the_user.password,'password')





if __name__=='__main__':
    unittest.main()
