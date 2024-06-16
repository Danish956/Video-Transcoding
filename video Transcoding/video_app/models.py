from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from Alpha_intern_LMS_app.models.customuser import*
from froala_editor.fields import FroalaField
from django.utils import timezone
from django.db import models
import pandas as pd
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count, Max
from django.db.models import Max, Sum, F

#====================================== Internship Data Model =======================================
class Internship_Data(models.Model):
    STATUS = (
            ('1','ACTIVE'),
            ('2','INACTIVE'),
          )
    internship_image = models.ImageField(upload_to='image/download/uploads/internship_image')
    internship_title = models.CharField(max_length=50)
    internship_position = models.CharField(max_length=50)
    internship_location = models.CharField(max_length=50) 
    internship_duration = models.CharField(max_length=50)
    internship_description = FroalaField(null=True, blank=True)
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True,default=0)
    status = models.CharField(max_length=25,choices=STATUS,default=1)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.internship_title
    

    def get_domain_absolute_url(self):
        from django.urls import reverse
        return reverse("internship_domain_detail", kwargs={'slug': self.slug})
    

    def get_discounted_price(self):
        if self.discount is not None:
            discounted_price = int(self.price - (self.price * self.discount / 100))
            return discounted_price
        else:
            return self.price

def create_slug(instance, new_slug=None):
    slug = slugify(instance.internship_title)
    if new_slug is not None:
        slug = new_slug
    qs = Internship_Data.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver, Internship_Data)
#==================================================================================================
#==================================================================================================




#============================= Lesson Model ================================================
class Internship_Lesson(models.Model):
    internship_data = models.ForeignKey(Internship_Data,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " _ " + self.internship_data.internship_title

#============================================================================================


#============================= Topic Model ==================================================
class Internship_Topic(models.Model):
    lesson = models.ForeignKey(Internship_Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    video_thumbnail = models.ImageField(upload_to='image/download/uploads/internship_video_thumbnail/', null=True, blank=True)
    video = models.FileField(upload_to="image/download/uploads/internship_video/original/", null=True, blank=True, max_length=255)
    video_360p = models.FileField(upload_to="image/download/uploads/internship_video/original/360p/", null=True, blank=True, max_length=255)
    video_480p = models.FileField(upload_to="image/download/uploads/internship_video/original/480p/", null=True, blank=True, max_length=255)
    video_720p = models.FileField(upload_to="image/download/uploads/internship_video/original/720p/", null=True, blank=True, max_length=255)
    video_1080p = models.FileField(upload_to="image/download/uploads/internship_video/original/1080p/", null=True, blank=True, max_length=255)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    