from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ContentManagement.models import BaseModel

# Create your models here.


class Country(BaseModel):
    title          = models.CharField(max_length=255)
    slug           = models.SlugField()
    def __str__(self):
        return self.title + ' - ' + self.slug


class State(BaseModel):
    title          = models.CharField(max_length=255)
    slug           = models.SlugField()
    country           = models.ForeignKey(Country,models.CASCADE)
    def __str__(self):
        return self.title + ' - ' + self.slug

class District(BaseModel):
    title          = models.CharField(max_length=255)
    slug           = models.SlugField()
    state           = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.slug


class Place(BaseModel):
    placename         = models.CharField(max_length=255)
    district          = models.ForeignKey(District,on_delete=models.CASCADE)
    slug               = models.SlugField(unique=True)
    description       = RichTextField()
    location          = models.CharField(max_length=255, blank=True,null=True)
    pincode           = models.IntegerField(blank=True,null=True)
    main_home_image   = models.ImageField(upload_to='places/',help_text='Please Upload the image size of 756 * 411', blank=True,null=True)
    def __str__(self):
        return self.placename