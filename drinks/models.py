from django.db import models

class DrinkType(models.TextChoices):
    IceCoffee = 'Ice Cofee', 'Ice Cofee'            # value, display name
    BlackCoffee = 'Black Cofee', 'Black Cofee'
    Capuccino = 'Capuccino', 'Capuccino'
    
    BlackTea = 'Black Tea', 'Black Tea'
    GreenTea = 'Green Tea', 'Green Tea'
    EnglishTea = 'English Tea', 'English Tea'

    OrangeJuice = 'Orange Juice', 'Orange Juice'
    AppleJuice = 'Apple Juice', 'Apple Juice'
    MangoJuice = 'Mango Juice', 'Mango Juice'

class DrinkSize(models.TextChoices):
    Small = 'Small'
    Medium = 'Medium'
    Large = 'Large'

class Drink(models.Model):
    type = models.CharField('Drink Type', max_length=100, choices=DrinkType.choices)
    size = models.CharField('Drink Size', max_length=25, choices=DrinkSize.choices)

    def __str__(self):
        return f"{self.size} {self.type}"
    
class Order(models.Model):
    drink = models.ForeignKey(Drink, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"[{self.created_at}] {self.drink} x {self.quantity}"