from pydantic import ValidationError
from fastapi import HTTPException
from typing import Dict

def valid_response(recipe_title:str, recipe_url:str) -> Dict[str, str]:

    return {'recipe_title': recipe_title, 'recipe_url': recipe_url}
    

def abort_bad_request(validation_errors:ValidationError.errors) -> None:
    raise HTTPException(status_code=400, 
                    detail=validation_errors)