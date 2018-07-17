import scrapy
import re
class QuotesSpider(scrapy.Spider):
    name = "swapnil"
    allowed_domains = ['livingsocial.com']
    start_urls = ['https://www.livingsocial.com/local/san-francisco']
    custom_settings = {
      'FEED_URI' : 'tmp/scrapy.sql'
                      }  

    def parse(self, response):
      titles = response.css('div.cui-udc-title ::text').re(r'[0-9A-Za-z].*')
      #titles = set(titles) #unordered 
      #image = response.css('img::attr(style)').extract()
      original_price = response.css('div.cui-udc-stacked-rows div.cui-price s.cui-price-original::text').extract()
      discount_price = response.css('div.cui-udc-details div.cui-udc-stacked-rows div.cui-price span.cui-price-discount::text').extract()
      discount_percentage = response.css('div.cui-udc-stacked-rows div.cui-promotions span.cui-discount::text').extract()
      discription =   response.css('div.cui-content div.cui-udc-details div.cui-description p.should-truncate ::text').extract()
      rating =  response.css('div.cui-udc-stacked-rows div.cui-review-rating ul.rating ::attr(data-bhc)').re(r'[0-9].*')
      rating_count = response.css('div.cui-udc-stacked-rows div.cui-review-rating div.rating-count ::attr(data-bhc)').re(r'[0-9].*')



      #extracted content row wise

      for item in zip(titles,original_price,discount_price,discount_percentage,discription,rating,rating_count):
          scraped_info = {
              'title' : [item[0]],
              #'image_urls' : [item[1]], #Set's the url for scrapy to download images
              'original price' : [item[1]],
              'discount_price' : [item[2]],
              'discount_percentage' : [item[3]],
              'discription' : [item[4]],
              'rating' : [item[5]],
              'rating_count' : [item[6]]
               }

          yield scraped_info
        
      next_page =  response.css('span.name a::attr(href)').extract()
      for item in(next_page):
          if item is not None:	
              next_page = response.urljoin(item)
              yield scrapy.Request(next_page, callback=self.parse)