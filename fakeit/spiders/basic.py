# -*- coding: utf-8 -*-
import scrapy
class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['fake-it.ws']
    start_urls = ['https://fake-it.ws/']
    def parse(self, response):
        
        yield{
            "name": ("name: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[1]/tbody/tr[1]/td/text()').extract())+"\n",
        "Address": ("address: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[1]/tbody/tr[2]/td/text()').extract())+"\n",
        "Street":("street: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[1]/tbody/tr[3]/td/text()').extract())+"\n",
        "Telephone":("telephone: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[1]/tbody/tr[4]/td/text()').extract())+"\n",
        "BirthDate":("birthdate: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[2]/tbody/tr[1]/td/text()').extract())+"\n",
        "Identity_Card": ("identity_card: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[3]/tbody/tr[1]/td/text()').extract())+"\n",
        "Identity_expiry":("identity_expiry: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[3]/tbody/tr[2]/td/text()').extract())+"\n",
        "Bank":("bank: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[4]/tbody/tr[1]/td/text()').extract())+"\n",
        "BLZ":("blz: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[4]/tbody/tr[2]/td/text()').extract())+"\n",
        "Account_Number":("account_number: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[4]/tbody/tr[3]/td/text()').extract())+"\n",
        "Iban":("iban: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[4]/tbody/tr[4]/td/div/div[1]/text()').extract())+"\n",
        "BIC":("bic: %s" % response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/table[4]/tbody/tr[5]/td/div/div[1]/text()').extract())+"\n"
        }
        