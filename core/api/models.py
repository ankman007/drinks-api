from django.db import models

class Drink(models.Model):
    CATEGORY_CHOICES = [
        ('cocktail', 'Cocktail'),
        ('beer', 'Beer'),
        ('wine', 'Wine'),
        ('non_alcoholic', 'Non-Alcoholic'),
        ('soft_drink', 'Soft Drink'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients_list = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default="Soft Drink")
    is_alcoholic = models.BooleanField(default=True)
    serving_size = models.CharField(null=True, blank=True, max_length=150)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}: {self.description}'

