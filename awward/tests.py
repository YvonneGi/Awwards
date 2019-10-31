from django.test import TestCase
from .models import Profile,Project,Rate
from django.contrib.auth.models import User


# Tests for Images model.
class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.photobooth= Project(id=1,image = '/static/images/wall.jpg',
        title ='Photobooth',description = 'Photo posting',link = 'https://photobooth-1.herokuapp.com/')
        self.juru = User(username='juru')
        # self.juru.save_username()
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photobooth,Project))

    # Testing Save Method
    def test_save_method(self):
        self.photobooth.save_image()
        image = Project.objects.all()
        self.assertTrue(len(image) == 1)
    # Testing update Method   
    def test_update(self):
        self.photobooth.save_image()
        image = Project.objects.filter(title = "Photobooth").first()
        update = Project.objects.filter (id=image.id).update(title = "Instagram_clone")
        updated = Project.objects.filter(title = "Instagram_clone").first()
        self.assertTrue(Project.title,updated.title)
    # Testing delete Method
    def test_delete(self):
        self.photobooth.save_image()
        image = Project.objects.filter(title="Photobooth").first()
        delete = Project.objects.filter(id=image.id).delete()
        image = Project.objects.all()
        self.assertTrue(len(image) ==0 )
    # Testing get all images Method
    def test_get_projects(self):
        images = Project.objects.all()
        self.assertTrue(Project.title)
    # Testing get images by category Method
    def test_search_by_title(self):
        self.photobooth.save_image()
        fetch_specific = Project.objects.get(title='Photobooth')
        self.assertTrue(fetch_specific.title=='Photobooth')

# Tests for Images model.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.juru= Profile(id=1,profile_pic = '/static/images/wall.jpg',
        fullname ='juru',bio = 'Developer',email = 'gi@gmail.com',phone_number = '07 83 99 99 00')
           
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.juru,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.juru= Profile(id=1,profile_pic = '/static/images/wall.jpg',
        fullname ='juru',bio = 'Developer',email = 'gi@gmail.com',phone_number = '07 83 99 99 00')
        self.juru.save_user_profile()
        Profile = Profile.objects.all()
        self.assertTrue(len(profile) == 1)
    # Testing update Method   
    def test_update(self):
        profile = Profile.objects.filter(fullname = "juru").first()
        update = Profile.objects.get(username_id=profile.username).update(fullname = "Gi")
        updated = Profile.objects.filter(fullname = "Gi").first()
        self.assertTrue(Profile.fullname,updated.fullname)

# Tests for Images model.
# class RateTestClass(TestCase):
#     # Set up method
#     def setUp(self):
#         self.juru = Profile(id=1,profile_pic = '/static/images/wall.jpg',
#         fullname ='juru',bio = 'Developer',email = 'gi@gmail.com',phone_number = '07 83 99 99 00')
           
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.juru,Profile))








