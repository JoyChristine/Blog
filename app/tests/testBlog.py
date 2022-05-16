import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(id=1,blog_title='Test Blog',content='This is a test blog',user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))