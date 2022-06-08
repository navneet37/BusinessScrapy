# Business scrapper
Scrapes data and stores data in database

## install required dependencies 
pip install -r requirements.txt

# How to run
scrapy crawl business

### Run with storing in json file 
scrapy crawl business -O biz_sample.json

### To check data in database run show_table.py file
python show_table.py
