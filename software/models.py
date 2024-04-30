from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils import timezone
#from encrypted_fields import EncryptedCharField
#from django.contrib.auth.hashers import make_password
#from django.conf  import settings


class Software(models.Model):
    #id_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    license = models.IntegerField(default=123456789)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="1", verbose_name='Allowed users')
    owner = models.CharField(max_length=200)
    s_accessible_by_all = models.BooleanField(default=False, verbose_name='Accessible by all users')
    #allowed_users = models.ManyToManyField(User, blank=True, verbose_name='Allowed users')

    def __str__(self):
        return self.name


"""class Document(models.Model):
    id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
"""

"""class Encryption(models.Model):
    encrypted_field = EncryptedCharField(max_length=100)
"""