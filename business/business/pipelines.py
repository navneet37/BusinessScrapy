# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class BusinessPipeline:
    def __init__(self):
        self.con = sqlite3.connect('business.db')
        self.cur = self.con.cursor()
        self.create_table()
        print("business pipe line initialised")

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS business(
        biz_id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
        business_name TEXT NOT NULL UNIQUE ,
        address1 TEXT ,
        contact_name TEXT,
        phone TEXT,
        website TEXT,
        social_links TEXT,
        desc TEXT
       );""")

    def get_or_none(self, item):
        adapter = ItemAdapter(item)
        if not adapter.get('description'):
            item['description'] = None
        if not adapter.get('social_links'):
            item['social_links'] = None
        if not adapter.get('contact'):
            item['contact'] = None
        if not adapter.get('contact_name'):
            item['contact_name'] = None
        if not adapter.get('site'):
            item['site'] = None

    def process_item(self, item, spider):
        self.get_or_none(item)
        self.cur.execute("""INSERT OR IGNORE into business 
        (business_name, address1,contact_name,phone, website, social_links, desc) 
        VALUES (?,?,?,?,?,?,?)""", (item['biz_name'], item['address'], item['contact_name'],
                                    item['contact'], item['site'], item['social_links'],
                                    item['description']))
        self.con.commit()
        return item
