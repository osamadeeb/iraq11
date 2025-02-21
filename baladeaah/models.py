from django.db import models
import datetime
import os
# Create your models here.

def filepath(request,filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" %(timenow,old_filename)

    return os.path.join('uploads/',filename)


class School(models.Model):
    name =models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    video = models.FileField(upload_to = 'photo/%y/%m/%d',default
     = "photo/25")
    file = models.ImageField(upload_to='photo/%y/%m/%d' ,null=True, blank = True)
    class Meta:
        db_table='school'


   




