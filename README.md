# RANDOM RECIPE REST API

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


