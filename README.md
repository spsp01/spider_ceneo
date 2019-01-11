# Spider Scrapy Ceneo

### Crawl Start
To run the crawl, type the command:
```
scrapy crawl ceneo
```


Crawler extracts the following data:

#### Category:
- id
- name
- parent category id

#### Product
- name
- category_id
- thumbnail_url
- url

#### Shop:
- name
- url
- thumbnail_url

#### Product price:
- shop_id
- product_id
- price
- price and shipment
- product_url
- score
- review_count

### Additional information
Exports scraped data  in 4 json files in the folder /scraped
