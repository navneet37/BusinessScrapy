# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class BusinessItem(scrapy.Item):
    # define the fields for your item here like:
    biz_name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    address = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    contact_name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    contact = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    site = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    social_links = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
