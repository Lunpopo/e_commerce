from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "user"
