from pydantic import BaseModel, validator
import random_recipes_api.meal_types_mapper as meal_types_mapper
from typing import List


class MealTypeValidator(BaseModel):
    meal_type: str

    @validator('meal_type')
    def meal_type_must_be_valid(cls, meal_type):
        meal_type = meal_type.lower().strip()
        
        possible_meal_types: List[str] = meal_types_mapper.get_possible_meal_types()
        
        if meal_type not in possible_meal_types:
            message: str = f'{meal_type} is not in possible meal types: '\
                           f"{', '.join(possible_meal_types)}"
            raise ValueError(message)
        return meal_type
