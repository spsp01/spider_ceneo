# -*- coding: utf-8 -*-

import scrapy


class CategoryItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    parent_category_id = scrapy.Field()

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    category_id = scrapy.Field()
    thumbnail_url = scrapy.Field()
    url = scrapy.Field()
    product_url = scrapy.Field()
    score = scrapy.Field()  # additional field
    review_count = scrapy.Field()  # additional field

class ShopItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    thumbnail_url = scrapy.Field()

class ProductPriceItem(scrapy.Item):
    shop_id = scrapy.Field()
    product_id = scrapy.Field()
    price = scrapy.Field()
    price_and_shipment = scrapy.Field()
    product_url = scrapy.Field()
