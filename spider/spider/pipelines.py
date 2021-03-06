# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter


class SpidPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesExportPipeline(object):

    def __init__(self):
        self.category_seen = set()
        self.product_seen = set()
        self.shop_seen = set()
        self.product_price_seen = set()

    def open_spider(self, spider):
        # Creates 4 files for storage scraped items
        self.category_file = open('spider/scraped/category.json', 'wb')
        self.category_exporter = JsonItemExporter(self.category_file, encoding="utf-8")
        self.category_exporter.start_exporting()
        self.product_file = open('spider/scraped/product.json', 'wb')
        self.product_exporter = JsonItemExporter(self.product_file, encoding="utf-8")
        self.product_exporter.start_exporting()
        self.shop_file = open('spider/scraped/shop.json', 'wb')
        self.shop_exporter = JsonItemExporter(self.shop_file, encoding="utf-8")
        self.shop_exporter.start_exporting()
        self.product_price_file = open('spider/scraped/productprice.json', 'wb')
        self.product_price_exporter = JsonItemExporter(self.product_price_file, encoding="utf-8")
        self.product_price_exporter.start_exporting()

    def close_spider(self, spider):
        # Closing exports and scraped item files

        self.category_exporter.finish_exporting()
        self.category_file.close()
        self.product_exporter.finish_exporting()
        self.product_file.close()
        self.shop_exporter.finish_exporting()
        self.shop_file.close()
        self.product_price_exporter.finish_exporting()
        self.product_price_file.close()

    def process_item(self, item, spider):

        if 'id' in item.keys() and 'name' in item.keys() and 'parent_category_id' in item.keys():
            # Drops duplicates in category
            if item['id'] in self.category_seen:
                raise DropItem("Duplicate category item found: %s" % item)
            else:
                self.category_seen.add(item['id'])
                # Exports category item
                self.category_exporter.export_item(item)
                return item

        if 'name' in item.keys() and 'category_id' in item.keys() and 'thumbnail_url' in item.keys() and 'url' in item.keys():
            # Drops duplicates in products

            if item['url'] in self.product_seen:
                raise DropItem("Duplicate product item found: %s" % item)
            else:
                self.product_seen.add(item['url'])
                # Exports category item
                self.product_exporter.export_item(item)
                return item

        if 'name' in item.keys() and 'url' in item.keys() and 'thumbnail_url' in item.keys():
            # Drops duplicates in shops
            if item['url'] in self.shop_seen:
                raise DropItem("Duplicate shop item found: %s" % item)

            else:
                self.shop_seen.add(item['url'])
                # Exports shop item
                self.shop_exporter.export_item(item)
                return item

        if 'shop_id' in item.keys() and 'product_id' in item.keys() and 'price' in item.keys() and 'price_and_shipment' in item.keys():
            # Drops duplicates in product price

            if item['shop_id'] + '-' + item['product_id'] in self.product_price_seen:
                raise DropItem("Duplicate product price item found: %s" % item)
            else:
                self.product_price_seen.add(item['shop_id'] + '-' + item['product_id'])
                # Exports product price item
                self.product_price_exporter.export_item(item)
                return item

        return item
