from django.db import models
from django.contrib.auth.models import User, Group

class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category


UNIT_CHOICES = [
    ('kg', 'Kilograms'),
    ('g', 'Grams'),
    ('L', 'Liters'),
    ('pcs', 'Piece'),
    ('pack', 'Pack'),
    ('can', 'Cane')
    # Add more units as needed
]


class Item(models.Model):
    item_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_of_measurement = models.CharField(max_length=50, choices=UNIT_CHOICES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_quantity = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def needs_reorder(self):
        return self.quantity < self.min_quantity

    def __str__(self):
        return f"{self.item_name} ({self.quantity} {self.unit_of_measurement})"


# Using Django's built-in User model for authentication
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

