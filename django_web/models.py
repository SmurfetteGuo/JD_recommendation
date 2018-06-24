from django.db import models

# Create your models here.
class DjangoWebProductmessage(models.Model):
    title = models.TextField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    url=models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_web_productmessage'
