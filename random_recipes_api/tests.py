from random_recipes_api.validators import MealTypeValidator

class TestValidator:
    
    def test_validator_valid_meal_type(self):
        valid_meal_type:str = 'Main_Courses'
        validated_data = MealTypeValidator.meal_type_must_be_valid(valid_meal_type)
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
    
    def test_validator_valid_meal_type_with_whitespaces(self):
        valid_meal_type:str = '   Main_courses   '
        validated_data = MealTypeValidator.meal_type_must_be_valid(valid_meal_type)
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
        