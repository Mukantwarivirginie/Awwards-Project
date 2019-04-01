from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    image= models.ImageField(upload_to='photo/') 
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    editor = models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name
    def save_profile(self):
        self.save()
    
   
    def display_profile(self):
        self.display()
    
    
    @classmethod
    def get_profile(cls,id):
        return Profile.objects.get(id=id)




    
class Comments(models.Model):
    name  = models.Field(max_length =30)
    bio = models.CharField(max_length =30)
    def __str__(self):
        return self.name


    @classmethod
    def search_by_category(cls,name):
        category = cls.objects.filter(image_name__icontains=image_name).first()
        images=Image.objects.filter(category=category)
        return images
     
class Follow(models.Model):
    name= models.CharField(max_length =30)
    bio = models.CharField(max_length =30) 
    def __str__(self):
        return self.name


class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image = models.ImageField(upload_to='photo/') 
    like= models.TextField()

     
 
 
    def __str__(self):
        return self.image
    def save_image(self):
        self.save()
    
   
    def display_image(self):
        self.display()
    
    
    @classmethod
    def get_image(cls,id):
        return Image.objects.get(id=id)


    @classmethod
    def search_by_title(cls,search_term):
        photo = cls.objects.filter(image_name__icontains=search_term)
        return photo

class NewArticleForm(models.Model):
    image = models.CharField(max_length =30)
    picture = models.ImageField(upload_to='photo/') 
    like= models.TextField()










