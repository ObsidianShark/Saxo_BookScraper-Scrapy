# Saxo Book Scraper



## Description

This spider will crawl all books currently listed as bestsellers over the first 10 pages to collect data for further analysis.

## Requirements

Python 3.10+\
Docker


## Installation

To clone the repository, type the code below in a shell :

```bash
  git clone https://github.com/ObsidianShark/Saxo_BookScraper-Scrapy.git  
```

To install dependencies, run the command bellow :

```bash
  pip install -r requirements.txt
```

To properly use the scrapy-splash dependency, splash docker is necessary so make sure to check all the settings configuration at: https://github.com/scrapy-plugins/scrapy-splash

## Usage

Start your splash docker with the command bellow:

```bash
  docker run -p 8050:8050 scrapinghub/splash
```

To crawl over best selling books from saxo.com, run the command bellow:

```bash
  scrapy crawl saxo -o saxo.json
```
