from dataclasses import dataclass
from enum import Enum

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
    SAUCE = 7

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
    def __init__(self, name:str, meals:list[Meal], typical_seasons: list[Season], prep_time_min:int, cold:bool = False, ingredients:list[Ingredient]=[]) -> None:
    
        self.name = name
        self.ingredients: list[Ingredient] = ingredients
        self.meals: list[Meal] = meals
        self.score: int = 0
        self.cold: bool = cold
        self.seasons:list[Season] = typical_seasons
        self.prep_time_min: int = prep_time_min

    def __repr__(self) -> str:
        ingredients = [f'{i.food.name}: {i.quantity_1person}g' for i in self.ingredients ]
        return f'Recipe: {self.name}\nIngredients: {ingredients}'
    
    def add_ingredient(self, ing:Ingredient):
        self.ingredients.append(ing)

    
    def for_N_people(self, n:int)->list[(str,float)]:
        """Calculate quantities for N people"""
        return [(i.food.name,n*i.quantity_1person) for i in self.ingredients]




