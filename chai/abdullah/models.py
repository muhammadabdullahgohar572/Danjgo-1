from django.db import models

from django.utils import timezone
# Create your models here.
class chaiVartity(models.Model):
    name=models.CharField(max_length=100)
    imge=models.ImageField(upload_to='chai')
date_added=models.DateTimeField(default=timezone.now)