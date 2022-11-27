from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User (or refer to settings)




class Country(models.Model):
    name=models.CharField(max_length=30)
    abbr=models.CharField(max_length=5)
    is_active=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    class Meta:
        #db_table='Countries'
        verbose_name='Country'
        verbose_name_plural='Countries'





class Profile(models.Model):
    user=models.OneToOneField(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone_number=models.BigIntegerField(blank=True,null=True,unique=True)
    country=models.ForeignKey(to=Country,on_delete=models.CASCADE)
    avatar=models.ImageField(blank=True,upload_to='profile_avatars/')



class Device(models.Model):
    DEVICE_WEB= 1
    DEVICE_IOS= 2
    DEVICE_ANDROID= 3
    DEVICE_PC= 4
    DEVICE_TYPE_CHOICES=(
        (DEVICE_WEB,'web'),
        (DEVICE_IOS,'ios'),
        (DEVICE_ANDROID,'android'),
        (DEVICE_PC,'pc')
    )
    user=models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='devices',on_delete=models.CASCADE)
    device_uuid=models.UUIDField('DEVICE UUID',null=True)
    last_login=models.DateTimeField('last login date',null=True)
    device_type=models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    device_os=models.CharField('device os',max_length=10,blank=True)
    device_model=models.CharField('device model',max_length=20,blank=True)
    app_version=models.CharField('app version',max_length=5,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)








