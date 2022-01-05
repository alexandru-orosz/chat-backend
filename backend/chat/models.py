from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    imageUrl = models.URLField(max_length=500)

    def __str__(self):
        return self.username


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    text = models.CharField(max_length=500, null=True)
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    imageUrl = models.URLField(max_length=300, null=True)

    def __str__(self):
        return "%s: %s" % (self.fromUser.username, self.text)

