from django.db import models
from group.models import Group

class Post(models.Model):

    title    = models.CharField(max_length=200)
    creator  = models.CharField(max_length=200)
    group    = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="posts")
    content  = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    creator  = models.CharField(max_length=200)
    content  = models.TextField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    post     = models.ForeignKey(Post,on_delete=models.DO_NOTHING,related_name="comment")

    def __str__(self):
        return self.content

class SubComment(models.Model):
    creator  = models.CharField(max_length=200)
    content  = models.TextField()
    photo    = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    comment  = models.ForeignKey(Comment,on_delete=models.DO_NOTHING,null=True,related_name="sub_comment")
    sub_comment = models.ForeignKey("self",on_delete=models.DO_NOTHING,null=True,blank=True,related_name="meta_comment")

    def __str__(self):
        return self.content


