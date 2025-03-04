from django.db import models

from django.utils import timezone
# Create your models here.
class chaiVartity(models.Model):
    CHAI_TYPE_CHOICES = [
            ('ML','Masla'),
            ('FL','Fava'),
            ('CL','Cinnamon'),
            ('OL','Olive'),
            ('OL','Other')
    ]
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    imge=models.ImageField(upload_to='chai')
    date_added=models.DateTimeField(default=timezone.now)
    type_chai=models.CharField(max_length=100 ,choices=CHAI_TYPE_CHOICES) 



    def __str__(self):
        return self.name