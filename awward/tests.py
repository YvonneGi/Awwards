from django.test import TestCase
from .models import Profile,Post,Follow,Comment,Like
from django.contrib.auth.models import User

# Tests for Posts model.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(instance):
        instance.fina= Profile(id=1,profile_pic = '/static/images/insta-screen.png',fullname = 'Fina',
        bio='Crazy',email='gi@gmail.com')
        
    # Testing  instance
    def test_instance(instance):
        instance.assertTrue(isinstance(instance.fina,Profile))
    # Testing Save Method
    def test_save_method(instance):
        instance.fina= Profile(id=1,profile_pic = '/static/images/insta-screen.png',fullname = 'Fina',
        bio='Crazy',email='gi@gmail.com')
        instance.fina.save_user_profile(instance)
        profile = Profile.objects.all()
        instance.assertTrue(len(profile) == 1)
    # Testing update Method   
    def test_update(instance):
        instance.fina.save_user_profile(instance)
        profile = Profile.objects.filter(fullname = "Fina").first()
        update = Profile.objects.filter (id=profile.id).update(fullname = "Anna")
        updated = Profile.objects.filter(fullname = "Anna").first()
        instance.assertTrue(updated.fullname)
    # Testing delete Method
    def test_delete(instance):
        instance.fina.save_user_profile(instance)
        username = Profile.objects.filter(fullname="Fina").first()
        delete = Profile.objects.filter(id=username.id).delete()
        username = Profile.objects.all()
        instance.assertTrue(len(username) ==0 )

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.dreams= Post(id=1,photo = '/static/images/cb7.jpg',caption = 'Dreams')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.dreams,Post))
    #Testing Save Method
    def test_save_method(self):
        self.dreams= Post(id=1,photo = '/static/images/cb7.jpg',caption = 'Dreams')
        self.fina.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) == 1)
    # Testing update Method   
    def test_update(self):
        self.dreams.save_photo()
        post = Post.objects.filter(caption = "Dreams").first()
        update = Post.objects.filter (id=post.id).update(caption = "Amazing")
        updated = Post.objects.filter(caption = "Amazing").first()
        self.assertTrue(updated.caption)
    # # # Testing delete Method
    def test_delete(self):
        self.dreams.save_photo()
        username = Profile.objects.filter(fullname="Fina").first()
        delete = Profile.objects.filter(id=username.id).delete()
        username = Profile.objects.all()
        self.assertTrue(len(username) ==0 )

class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.amazing= Comment(comment_content = 'Amazing')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.amazing,Comment))
    # Testing Save Method
    def test_save_method(self):
        self.amazing.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)
    # Testing delete Method
    def test_delete(self):
        self.amazing.save_comment()
        comment = Comment.objects.filter(comment_content="Amazing").first()
        delete = Comment.objects.filter(id=comment.id).delete()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) ==0 )


class FollowTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kk= Follow(follow = 'kk')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kk,Follow))
    # Testing Save Method
    def test_save_method(self):
        self.kk.save_follow()
        follows = Follow.objects.all()
        self.assertTrue(len(follows) > 0)

class LikeTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kk = Like(control = 'kk')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kk,Like))
    # Testing Save Method
    def test_save_method(self):
        self.kk.save_like()
        likes = Like.objects.all()
        self.assertTrue(len(likes) > 0)


