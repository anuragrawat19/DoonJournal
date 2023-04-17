from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# Create your models here.
class BaseModel(models.Model):
    ACTIVE_CHOICES = ((0, 'Inactive'), (2, 'Active'),)
    active = models.PositiveIntegerField(choices=ACTIVE_CHOICES,default=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Section(BaseModel):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(unique=True)


    def __str__(self):
        return self.title


class Article(BaseModel):
    art_title         = models.CharField(max_length=255)
    main_home         = models.BooleanField(default=False)
    section           = models.ForeignKey(Section,on_delete=models.CASCADE)
    slug              = models.SlugField(unique=True)
    description       = RichTextField()
    source            = models.CharField(max_length=255, blank=True,null=True)
    release_date      = models.DateTimeField()
    release_by        = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    main_home_image   = models.ImageField(upload_to='articlehome/',help_text='Please Upload the image size of 756 * 411', blank=True,null=True)
    image_icon        = models.ImageField(upload_to='articleicon/',help_text='Please Upload the image size of 154 * 125',blank=True,null=True)
    def __str__(self):
        return self.art_title

class ContactUs(BaseModel):
    name         = models.CharField(max_length=255)
    phone           = models.CharField(max_length=255)
    email           = models.EmailField()
    message            = models.TextField()
    def __str__(self):
        return self.name + ' - ' + self.email

class ContentSection(BaseModel):
    title          = models.CharField(max_length=255)
    slug           = models.SlugField()
    description       = RichTextField()
    
    def __str__(self):
        return self.title + ' - ' + self.slug

class Images(BaseModel):
    slug           = models.SlugField()
    image          = models.ImageField(upload_to='sectionimages/',blank=True,null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,blank=True,null=True)
    object_id = models.PositiveIntegerField(blank=True,null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return  self.slug