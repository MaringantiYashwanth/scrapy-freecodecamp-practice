import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            next_page = response.css('li.next a::attr(href)').get()
            if 'catalogue' in next_page:
                    next_page_url = 'https://books.toscrape.com/' + relative_url
                else:
                    next_page_url = 'https://books.toscrape.com/catalogue/' + relative_url
                yield response.follow(next_page_url, callback=self.parse)