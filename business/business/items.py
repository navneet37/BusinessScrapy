# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import urllib.parse

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity
from w3lib.html import remove_tags


def contact_cleaning(contact_value):
    if contact_value is not " ":
        return contact_value


def clean_slinks(slinks):
    slinks_new = urllib.parse.unquote(slinks.split("?URL=")[-1])
    return slinks_new


def address_clean(add):
    if add:
        return add


class BusinessItem(scrapy.Item):
    # define the fields for your item here like:
    biz_name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    address = scrapy.Field(input_processor= address_clean, output_processor=Join())
    contact_name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    contact = scrapy.Field(input_processor=MapCompose(contact_cleaning, str.strip), output_processor=TakeFirst())
    site = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    social_links = scrapy.Field(input_processor=MapCompose(clean_slinks), output_processor=Join())
    description = scrapy.Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
