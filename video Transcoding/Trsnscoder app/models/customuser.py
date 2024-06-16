from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session

#====================================== User Model ================================================
class CustomeUser(AbstractUser):
    STATUS = (
          ('1','ACTIVE'),
          ('2','INACTIVE'),
          )
    USER_TYPE = (
          ('1','SUPERADMIN'),
          ('2', 'STUDENT'),
          )
    profile_image = models.ImageField(upload_to='image/download/uploads/user_image/',null=True,blank=True)
    dob = models.CharField(max_length=50,null=True,blank=True)
    mobile_number = models.CharField(max_length=50,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(max_length=50000,null=True,blank=True)
    zipcode = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    twitter =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    facebook =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    instagram =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    youtube =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    linkedin =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    github =  models.URLField(max_length=250000000000000000000000,null=True,blank=True)
    status = models.CharField(max_length=25,choices=STATUS,default=2)
    user_type = models.CharField(max_length=25,choices=USER_TYPE,default=3)
    decrypt_password = models.CharField(max_length=25,default='')
    date_and_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#==================================================================================================
#==================================================================================================
    

