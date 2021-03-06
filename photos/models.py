from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    def save_Category(self):
        self.save()
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
    def save_photo(self):
        self.save()

    def search_photos(category):
        photos = Photo.objects.filter(category__name__icontains=category)
        return photos        