# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'



ROBOTSTXT_OBEY = True
LOG_LEVEL = 'INFO'


ITEM_PIPELINES = {
    'spider.pipelines.SpidPipeline': 300,
    'spider.pipelines.DuplicatesExportPipeline':800,
}

FEED_EXPORTERS = {
 'jsonlines': 'scrapy.contrib.exporter.JsonItemExporter',
}
FEED_FORMAT = 'json'
FEED_URI = "tmp/result-%(time)s.json"