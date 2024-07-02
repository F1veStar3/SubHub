from django.core.validators import MaxValueValidator
from django.db import models

from clients.models import Client


class Services(models.Model):
    name = models.CharField(max_length=200)
    full_price = models.IntegerField()


class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount'),
    )

    plan_type = models.CharField(max_length=15, choices=PLAN_TYPES)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])


class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name="subscriptions", on_delete=models.CASCADE)
    service = models.ForeignKey(Services, related_name="subscriptions", on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name="subscriptions", on_delete=models.CASCADE)
