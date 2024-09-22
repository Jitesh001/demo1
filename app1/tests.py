from django.test import TestCase
from .models import Post
# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title='Test Post', author='John Doe', slug='test-post')

    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author, 'John Doe')
    
    def test_post_created(self):
        post = Post.objects.get(title='Test Post')
        self.assertIsNotNone(post.slug)