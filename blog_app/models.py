from django.db import models
from django.utils import timezone
from django.urls import  reverse

# Create your models here.

class post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_cmnts(self):
        return self.comments.filter(approved_stat=True)

    def get_absolute_url(self):
        return reverse('blog_app:post_dtl',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey('post',related_name ='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_stat = models.BooleanField(default=False)


    def approve(self):
        self.approved_stat = True
        self.save()

    def get_absolute_url(self):
        return reverse('/')

    def __str__(self):
        return self.text
