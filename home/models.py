from django.db import models


class Home(models.Model):
    logo = models.ImageField(upload_to='logo')
    background_image = models.ImageField(upload_to='background-image')
    head = models.CharField(max_length=150)
    sub_head = models.CharField(max_length=150)
    next_sub_head = models.CharField(max_length=150)

    def __str__(self):
        return self.head
