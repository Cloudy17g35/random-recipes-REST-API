from pydantic import BaseModel, validator
import random_recipes_api.meal_types_mapper as meal_types_mapper
from typing import List


class MealTypeValidator(BaseModel):
    meal_type: str

    @validator('meal_type')
    def meal_type_must_be_valid(cls, meal_type):
        meal_type = meal_type.lower().strip()
        
        possible_meals: List[str] = meal_types_mapper.get_possible_meal_types()
        
        if meal_type not in possible_meals:
            message: str = f'{meal_type} is not in possible_books: '\
                           f"{', '.join(possible_meals)}"
            raise ValueError(message)
        return meal_type.lower().strip()

