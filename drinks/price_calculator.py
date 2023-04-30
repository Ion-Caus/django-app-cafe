from .models import Drink, Order, DrinkSize, DrinkType

def order_price(order: Order):
    return calculateDrinkPrice(order.drink) * order.quantity

def calculateDrinkPrice(drink: Drink):
    return drinkTypePrice(drink.type) + drinkSizeCoefficient(drink.size)

def drinkSizeCoefficient(size: DrinkSize):
    coefficients = {
        DrinkSize.Small: 1,
        DrinkSize.Medium: 1.5,
        DrinkSize.Large: 2,
    }

    return coefficients[size]
    

def drinkTypePrice(type: DrinkType):
    prices = {
        DrinkType.IceCoffee: 50.5,
        DrinkType.BlackCoffee: 45.0,
        DrinkType.Capuccino: 55.0,

        DrinkType.BlackTea: 40.0,
        DrinkType.GreenTea: 35.5,
        DrinkType.EnglishTea: 45.75,

        DrinkType.OrangeJuice: 60.0,
        DrinkType.AppleJuice: 55.0,
        DrinkType.MangoJuice: 65.0,
    }

    return prices[type]