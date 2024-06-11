from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True , blank= True)
    email = models.EmailField(null=True , blank= True)
    address = models.TextField(null=True , blank= True)

class Products(models.Model):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=40)
    publish_date = models.DateField()

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()

    def sung_by(self):
        return ",".join([str(p) for p in self.user.all()])
    
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy=True

class CommonInfo(models.Model):
    Name = models.CharField(max_length=70)
    Age = models.IntegerField(null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

class Dealer(models.Model):
    name= models.CharField(max_length=40)
    niche = models.CharField(max_length=30, null= True)
    sale= models.IntegerField()

class Quality(models.Model):
    quality = models.CharField(max_length=100)
    is_good = models.BooleanField(default=True)
    is_bad = models.BooleanField(default=False)


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title
    
    

