import scrapy
from legobricks.items import LegobricksItem

class LegoBrickSets(scrapy.Spider):
    name = 'lego_brick_spider'
    
    def start_requests(self):
        urls = ['https://www.amazon.com/s?k=lego&rh=n%3A165793011%2Cp_89%3ALEGO&dc&qid=1599551783&rnid=2528832011&ref=sr_nr_p_89_1',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
         
    def parse(self, response):
        
       item = LegobricksItem()
        
       item['setname'] = response.xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/span/text()').extract()
       item['cost'] = response.xpath('//span[@class="a-price"]/span[@class="a-offscreen"]/text()').extract()
       item['age'] = response.xpath('//div[@class="a-row a-size-base a-color-base"]/span[@dir="auto"]/text()').extract()     
    
       data = zip(item['setname'], item['cost'], item['age'])   
       for obj in data:
         yield {
                    'set name' : obj[0],
                    'cost' : obj[1],
                    'age' : obj[2]
                
                    }

    next_page_xpath = '.next a ::attr(href)'
    next_page = response.xpath(next_page_xpath).extract_first()
    if next_page:
        yield scrapy.Request(
        response.urljoin(next_page),callback=self.parse)      