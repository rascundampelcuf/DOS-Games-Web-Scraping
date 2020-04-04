
import requests
import csv
from bs4 import BeautifulSoup
from game import Game


class Scraper():
      
    def __init__(self):
        self.url = 'http://www.dosgamesarchive.com/games/'
        self.games = []
          
    def __download_html(self, url):
        # Get data from url
        html = requests.get(url)
        self.status_code = html.status_code
        
        # Convert HTML content to BeautifulSoup object
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup
    
    def __get_games_table(self, page):
        # Get games from table with 'table_games' tag
        table_games = page.find('table', {'class': 'table_games'})
        games = table_games.findAll('tr')
        games.pop(0) # First element contains the table headers
        return games
    
    def scrape(self):
        print('Web scraping of classic games by "DOSGAMES"...')
        page = self.__download_html(self.url)
        games = self.__get_games_table(page)
        
scraper = Scraper()
scraper.scrape()