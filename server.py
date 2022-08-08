from fastapi import FastAPI
from random_recipes_api import controllers

app:FastAPI = FastAPI()

@app.get('/recipes/random_recipe/')
async def get_random_recipe(meal_type:str):
    return controllers.get_random_recipe(meal_type)