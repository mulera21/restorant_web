from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salad", "Salad"),
    ("main_dishes", "Main_dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "unavailable"),
    (1, "available")
)


class Item(models.Model):
    meal = models.CharField(max_length=10000, unique=True)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
