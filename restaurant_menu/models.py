from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)

STATUS=(
    (0,"Unavailable"),
    (1,"Available"),
)

class Item(models.Model):
    meal = models.CharField(max_length=255, unique=True)  # shorter max_length is better for names
    description = models.TextField(max_length=2000)  # TextField for long descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2)  # must include max_digits
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPE)  # use choices=
    #many to one relationship:one cook-> many items
    #all meals that the user created will be deleted
    #models.PROTECT:This prevents deletion of that User until all related Items are either deleted or reassigned
    #models.SET_NULL the user will be NULL, the items will be there;the author will be not associated
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # must include on_delete
    status = models.IntegerField(choices=STATUS,default=0)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal} ({self.meal_type})"
