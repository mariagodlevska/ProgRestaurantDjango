from django.db import models
import os, uuid
    

class WhyUs(models.Model):
    reason_number = models.SmallIntegerField()
    title = models.CharField(max_length=50, unique = True, db_index = True)
    description = models.TextField(max_length=500)
    position = models.SmallIntegerField(unique = True)
    is_visible = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return f'{self.title}'

    
class Category(models.Model):
    title = models.CharField(max_length=50, unique = True, db_index = True)
    position = models.SmallIntegerField(unique = True)
    is_visible = models.BooleanField(default = True)
    
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        ordering = ('position', )
    

class Dish(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split('.')[-1]
        file_name= f'{uuid.uuid4().text}'
        return os.path.join('dishes/%Y_%m_%d/', file_name)
    
    title = models.CharField(max_length=50, unique = True, db_index = True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default = True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        ordering = ('category', 'position')
 
    
class Events(models.Model):  
    title = models.CharField(max_length=50, unique = True, db_index = True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default = True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    

class PhotoGallery(models.Model):
    photo = models.ImageField(blank=True)
    is_visible = models.BooleanField(default = True)
    
    
class Chefs(models.Model):
    name = models.CharField(max_length=50, unique = True, db_index = True)
    photo = models.ImageField(blank=True)
    profession = models.CharField(max_length=50, db_index = True)
    position = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ('position', )
    
    
class Feedback(models.Model):
    name = models.CharField(max_length=50, unique = True, db_index = True)
    photo = models.ImageField(blank=True)
    profession = models.CharField(max_length=50, db_index = True)
    is_visible = models.BooleanField(default = True)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    position = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    

