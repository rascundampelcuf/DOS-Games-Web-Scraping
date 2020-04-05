
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
    
    def __get_max_page(self, page):
        pagination = page.find('div', 'pagination_top')
        list_pages = pagination.findAll('li')
        return int(list_pages[-2].find('a').string)
        
    def __get_table_games(self, page):
        # Get games from table with 'table_games' tag
        table_games = page.find('table', {'class': 'table_games'})
        games = table_games.findAll('tr', recursive=False)
        games.pop(0) # First element contains the table headers
        return games
    
    def __get_info_from_game(self, game):
        cells = game.findAll('td', recursive=False)
        the_game = Game(
            title = cells[1].find('a').string,
            violence = bool(cells[1].find('td', 'violence')),
            category = cells[2].find('a').string,
            year = cells[4].find('a').string
        )
        self.games.append(the_game)
    
    def scrape(self):
        print('Web scraping of classic games by "DOSGAMES"...')
        page = self.__download_html(self.url)
        max_page = self.__get_max_page(page)
        
        first = True        
        for i in range(1, max_page + 1):
            print('Scraping page', i)
            if first:
                first = not first
            else:
                page = self.__download_html(self.url + str(i) + '/')
        
            games = self.__get_table_games(page)
            for game in games:
                self.__get_info_from_game(game)
       
    def data2csv(self, filename):
        # Overwrite to the specified file.
        # Create it if it does not exist.
        csvwriter = csv.writer(open("../data/" + filename, "w", newline='\n', encoding="utf-8"))
        
        # Dump all the data with CSV format
        csvwriter.writerow(['Title', 'Category', 'Year', 'Violence'])
        for game in self.games:
            csvwriter.writerow(game.get_list())
