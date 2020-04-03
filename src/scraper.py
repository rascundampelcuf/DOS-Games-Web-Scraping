
import requests
import csv
from bs4 import BeautifulSoup
from game import Game


class Scraper():
      
    def __init__(self):
        self.url = 'http://www.xtdos.com/'
        self.games = []
        self.categories = {}
          
    def __download_html(self, url):
        # Get data from url
        html = requests.get(url)
        self.status_code = html.status_code
        
        # Convert HTML content to BeautifulSoup object
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup
    
    def __get_categories_links(self, page):
        # Get categories links from 'cat-item' tag
        divs = page.findAll('li', 'cat-item')
        print(divs[0].value)
    
    def scrape(self):
        print('Web scraping of classic games by "XTDOS"...')
        page = self.__download_html(self.url)
        self.__get_categories_links(page)
        
scraper = Scraper()
scraper.scrape()