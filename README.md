# RANDOM RECIPE REST API


## HOW TO RUN

In order to run with docker:

**Step 1**
`docker build -t random_recipes_api .`


**Step 2**
`docker run -e AWS_ACCESS_KEY_ID=your_access_key -e AWS_SECRET_ACCESS_KEY=your_secret_access_key -p 8080:8080 random_recipes_api`


## DESCRIPTION
Enables to make GET request
`GET recipes/random_recipe?meal_type=`

Needs one parameter which is **meal_type**.

Returns recipe title and link in json format.

All recipes are scraped from [jadlonomia](https://www.jadlonomia.com/ "jadlonomia") - Polish website with wegan food.

In first place all the recipes need to be scraped. Script called `run_scraper.py` enables to make it. It scrapes all the recipes and stores it in **S3 bucket**.


Diagram:


![Image](https://github.com/Cloudy17g35/random-recipes-REST-API/blob/main/diagrams/Scraper_diagram.png)



After we have all recipes stored on S3 flow looks like on diagram showed below:

![Image](https://github.com/Cloudy17g35/random-recipes-REST-API/blob/main/diagrams/APIdiagram.png)

