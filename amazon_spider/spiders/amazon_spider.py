import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
