from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.




class Profile(models.Model):
    name = models.CharField(max_length =60)
    picture_Main_pic = models.ImageField(upload_to='photos/', blank=True) 
    bio = models.CharField(max_length =500)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()
    def display_profile(self):
        self.display()


    class Meta:
        ordering = ['name']



class Project(models.Model):
    
    title = models.CharField(max_length =30)
    picture_Main_pic = models.ImageField(upload_to='photos/',null=True) 
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()
    
   
    def display_project(self):
        self.display()

    def delete_project(self):
        self.delete()
    
    
    @classmethod
    def get_project(cls,id):
        return Project.objects.get(id=id)



    @classmethod
    def search_by_title(cls,search_term):
        projects=Project.objects.filter(title__icontains=search_term).all()
        return projects
     
 

    class Meta:
        ordering = ['title']


class SignUpRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


