<a><img src="https://www.adslzone.net/app/uploads/2019/11/MSDOS.jpg"></a>

# DOS Games Web-scraping

## Descripció
This is a personal mini-project of web scraping.

The objective of this project was to complete a Web Scraping in Python of the website *"[DOS GAMES ARCHIVE](https://www.dosgamesarchive.com/)"*. From this website a list of all the games has been created and a data set with the created data has been generated.

---

## Source files

```bash
────Web-scraping
    │
    ├───data
    │       data.csv
    │
    └───src
            game.py
            main.py
            scraper.py
```
- **data/data.csv**: Output dataset. It contains a list of books.
- **src/game.py**: It contains the implementation of Game class. It was created to easily manage the information of each game.
- **src/main.py**: Input. It starts the scraping process.
- **src/scraper.py**: It contains the implementation of Scraper class. Scraper class contains the necessary methods to generate the dataset with the data provided by *DOS GAMES ARCHIVE*.

---

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/rascundampelcuf/DOS-Games-Web-Scraping.git`

### Setup

- In order to be able to run the code you should install the following packages:
> `requests`
```shell
$ pip install requests
```
> `csv`
```shell
$ pip install csv
```
> `bs4`
```shell
$ pip install bs4
```

- Once installed, move to `src` folder and run:
```shell
$ python main.py
```

---