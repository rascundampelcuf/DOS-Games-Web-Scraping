
from scraper import Scraper

output_file = "data.csv"
scraper = Scraper()
scraper.scrape()
scraper.data2csv(output_file)