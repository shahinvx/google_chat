from django.db import models
from django.db.models import manager

# Create your models here.
class Chat_Groups(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False,unique=True)
    user_a = models.IntegerField(blank=True, null=True)
    user_b = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Chat_Groups'