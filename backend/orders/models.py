import uuid
from django.db import models


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=50)


class Order(models.Model):
    STATUS_CHOICES = (
        (1, 'New'),
        (2, 'Completed'),
        (3, 'Other'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manager = models.ForeignKey(Client, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    caption = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
