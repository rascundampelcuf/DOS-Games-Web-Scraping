
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
    
    def __is_the_game_violent(self, cell, the_game):
        violence = cell.find('td', 'violence')
        the_game._violence = bool(violence)
    
    def __get_title_from_game(self, cell, the_game):
        title = cell.find('a').string
        the_game._title = title
        
        self.__is_the_game_violent(cell, the_game)
        print(the_game)
    
    def __get_info_from_game(self, game):
        the_game = Game()
        cells = game.findAll('td')
        
        # print(cells[1])
        self.__get_title_from_game(cells[1], the_game)
        
    
    def scrape(self):
        print('Web scraping of classic games by "DOSGAMES"...')
        page = self.__download_html(self.url)
        games = self.__get_games_table(page)
        # for game in games:
        print(len(games))
        self.__get_info_from_game(games[0])
            # break
        
scraper = Scraper()
scraper.scrape()