from django.db import models

CATEGORY_CHOICES = [
    (
        'WEB_DEV','Web Development'
    ),
    (
        'ANDROID_DEV','Android Development'
    ),
    (
        'DATA_SCIENCE','Data Science'
    ),
]

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,default='WEB_DEV')
    image = models.ImageField(upload_to='blog_images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
    