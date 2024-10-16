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
    author = models.ForeignKey('auth.user',related_name='blogs',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,default='WEB_DEV')
    image = models.ImageField(upload_to='blog_images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey('auth.user',related_name='comments',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment on {self.blog.title}: {self.text[:20]}'
    
    
    
    