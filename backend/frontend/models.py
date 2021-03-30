from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    user_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user_name