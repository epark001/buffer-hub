from django.db import models

# Create your models here.


class GenEd(models.Model):

    gen-ed_name = models.CharField(max_length=50)
    gen-ed_des = models.CharField(max_length=150, default="This is a Popular gen-ed!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.gen-ed_name
