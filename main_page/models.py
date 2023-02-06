from django.db import models
    

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
    

class Dish(models.Model):
    title = models.CharField(max_length=50, unique = True, db_index = True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default = True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.title}'
 
    
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
    
    
class Feedback(models.Model):
    name = models.CharField(max_length=50, unique = True, db_index = True)
    photo = models.ImageField(blank=True)
    profession = models.CharField(max_length=50, db_index = True)
    is_visible = models.BooleanField(default = True)
    description = models.TextField(max_length=500)
    rating = models.IntegerField()
    position = models.CharField(max_length=200)
    
    

