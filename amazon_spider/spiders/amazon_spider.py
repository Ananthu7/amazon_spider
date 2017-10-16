import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('div.s-item-container'):
          yield {
            'name' : item.css('a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal::attr(title)').extract_first(),
            'description': item.css('a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal::attr(href)').extract_first(),
            'price': ''.join(item.css('span.a-size-base.a-color-price.s-price.a-text-bold::text').extract()),
            'image' : item.css('img.s-access-image.cfMarker::attr(src)').extract_first(),
          }  
        self.log('Done')