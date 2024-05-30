from dataclasses import dataclass
from enum import Enum
from datetime import timedelta

class Season(Enum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3

class FoodType(Enum):
    VEGETABLE = 0 
    MEAT = 1
    PASTA = 2 
    BREAD = 3 
    SPICE = 4 
    DIARY = 5
    FISH = 6

class Meal(Enum):
    BREAKFAST = 0
    LUNCH = 1
    DINNER = 2
    MORNING_BREAK = 3
    AFTERNOON_BREAK = 4


@dataclass
class Food:
    name: str #Nome dell'ingrediente "esempio: spaghetti, zucchine, Parmigiano..."
    type: FoodType
    calories_100g: float
    fridge: bool = False

@dataclass
class Ingredient:
    food: Food
    quantity_1person: float
    
    def __init__(self, food:Food, quantity_1p:float) -> None:
        self.food: Food = food
        if quantity_1p < 0.0:
            raise ValueError
        self.quantity_1person: float = quantity_1p


class Recipe:
    """Recipe for 1 person""" 
    def __init__(self, name:str, meal:Meal, typical_season: Season, prep_time:timedelta, cold:bool = False) -> None:
    
        self.name = name
        self.ingredients: list[Ingredient] = []
        self.meal: Meal = meal
        self.score: int = 0
        self.cold: bool = cold
        self.typical_season: Season = typical_season
        self.prep_time: timedelta = prep_time

    def for_N_people(self, n:int)->list[Ingredient]:
        """Calculate quantities for N people"""
        pass




