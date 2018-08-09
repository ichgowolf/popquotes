import scrapy

# quote.css("div.quoteText::text").extract_first()
# quote.css("div.quoteFooter a::text").extract()[1]


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.goodreads.com/quotes',
    ]

    def parse(self, response):
      for quote in response.css('div.quoteDetails'):
        yield {
            'text': quote.css("div.quoteText::text").extract_first(),
            'tags': quote.css("div.quoteFooter a::text").extract_first()
        
        }

      next_page = response.css('a.next_page::attr(href)').extract_first()
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)

   