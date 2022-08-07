from bs4 import BeautifulSoup
import requests
from typing import Tuple, Dict
from collections import defaultdict
PAGE_LIMIT = 50


class Scraper:
    '''Scraper made to get all recipes titles and links from site jadlonomia.com'''
    @staticmethod
    def get_all_articles(page_content:requests.Response.content):
        soup = BeautifulSoup(page_content, features='html.parser')
        recipe_list = soup.find('div', id="RecipeList", class_='kafelki')
        return recipe_list.find_all('article')

    @staticmethod
    def get_link_from_article(article):
        article_header = article.find('h2')
        link = article_header.find('a').attrs['href']
        return link

    @staticmethod
    def get_article_title(article):
        article_header = article.find('h2')
        return article_header.find('a').text

    
    def get_link_and_title(self, article) -> Tuple[str, str]:
        return self.get_link_from_article(article), self.get_article_title(article)
    
    
    def get_data_for_meal_type(self,meal_type:str) -> Dict[str, str]:
        page_number: int = 1
        result:Dict[str, str] = defaultdict(list)
        while page_number <= PAGE_LIMIT:
            
            currentURL: str = f'https://www.jadlonomia.com/rodzaj_dania/{meal_type}/page/{page_number}/'
            current_site_response = requests.get(currentURL)
            
            if not current_site_response.ok:
                break
            
            page_content = current_site_response.content
            articles = self.get_all_articles(page_content)
            for article in articles:
                link, title = self.get_link_and_title(article)
                result['link'].append(link); result['title'].append(title)
            
            page_number += 1
            print(f'Scraping data from site: {currentURL}')
        return  result