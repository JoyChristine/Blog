import unittest
from ..models import Blog,User,Comment 


class Blog(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username="blogger",password = 'banana')
        self.new_blog = Blog(blog_title = 'Test',content = 'Test',category = 'Test',author = self.new_user)
        self.new_comment = Comment(content = 'Test',category = 'Test',author = self)

    def teardown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title,'Test')
        self.assertEquals(self.new_blog.content,'Test')
        self.assertEquals(self.new_blog.category,'Test')
        self.assertEquals(self.new_blog.author,self.new_user)
        self.assertEquals(self.new_blog.comments,self.new_comment)
        self.assertEquals(self.new_blog.likes,self.new_like)
        self.assertEquals(self.new_blog.dislikes,self.new_dislike)

    
    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog(self):
        self.new_blog.save_blog()
        got_bloges = Blog.get_blog(1)
        self.assertTrue(len(got_bloges) == 1)

if __name__ ==  '__main__':
    unittest.main()