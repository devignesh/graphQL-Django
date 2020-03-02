from django.db import models


class Blogpost(models.Model):
    
    author = models.TextField(max_length=285, blank=True, null=True)
    title = models.CharField(max_length=285, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    published_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.author
    
class Comment(models.Model):
    
    author = models.ForeignKey(Blogpost, null=True, blank=True, on_delete=models.SET_NULL)
    comment = models.CharField(max_length=285, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    def __str__(self):
        return self.comment