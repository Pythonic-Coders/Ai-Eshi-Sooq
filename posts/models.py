from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Post(models.Model):
    user_id = models.ForeignKey(User,to_field='id', on_delete=models.CASCADE,default=1)
    post_title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    post_img = models.CharField(max_length=350)
    post_description = models.TextField()
    pric = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=10, default=0000000000)

    def __str__(self):
        return self.post_title