from django.test import TestCase

# Create your tests here.
from .models import Photo, Category

class CategoryTestClass(TestCase):
    '''
    test for category class
    '''
    
    #set up method
    def setUp(self):
        self.ugali = Category(category='food')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.ugali,Category))
        
    def test_save_method(self):
        self.ugali.save_category()
        category=Category.objects.filter(category='food').first()
        update = Category.objects.filter(id=category.id).update(category='food')
        updated= Category.objects.filter(category='food').first()
        self.assertTrue(Category.category,updated.category) 
        
class PhotoTestClass(TestCase):
    '''
    test for photo class
    '''
    
    # setup method
    def setUp(self):
        self.description= Photo(name='description')
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.description, Photo))
        
    #Testing Save method
    def test_save_method(self):
        self.description.save_photo()
        photos=Photo.objects.all()
        self.assertTrue(len(photos)>0)                 
     