from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



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
    section           = models.ForeignKey(Section,on_delete=models.CASCADE)
    description       = RichTextField()
    source            = models.CharField(max_length=255, blank=True,null=True)
    release_date      = models.DateTimeField()
    release_by        = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    main_home_image   = models.ImageField(upload_to='static/articlehome/',blank=True,null=True)
    image_icon        = models.ImageField(upload_to='static/articleicon/',blank=True,null=True)
    def __str__(self):
        return self.art_title
    