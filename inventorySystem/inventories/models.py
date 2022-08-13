from pydoc import describe
from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    # null is purely database related whereas blank is validation related
    # for IntegerFields we do not specify the max_length since its ignored
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False, default="")
    note = models.TextField(null=False, blank=False, default="")
    stock = models.IntegerField(null=False, blank=False, default=0)
    availability = models.BooleanField(default=False)

    supplier = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
