# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FakeitItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    street = scrapy.Field()
    telephone = scrapy.Field()
    birthdate = scrapy.Field()
    identity_card = scrapy.Field()
    identity_expiry = scrapy.Field()
    bank = scrapy.Field()
    blz = scrapy.Field()
    account_number = scrapy.Field()
    iban = scrapy.Field()
    bic = scrapy.Field()
