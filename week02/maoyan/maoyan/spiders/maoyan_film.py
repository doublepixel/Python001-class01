import scrapy

from maoyan.items import MaoyanItem


class MaoyanFilmSpider(scrapy.Spider):
    name = 'maoyan_film'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ["https://maoyan.com/films?showType=3",]

    def parse(self, response):
        film = MaoyanItem()
        print(response.text)
        dl = response.xpath('//div[@class="movie-item-hover"]')
        type(dl)
        for dd in dl:
            # 电影名称
            film["film_name"]= "".join(dd.xpath('./a/div/div[1]/span[1]/text()').extract()[0])
            # # 电影类型
            film["film_type"] = "".join(dd.xpath('./a/div/div[2]/text()').extract()[1]).strip()
            # 上映时间
            film["film_date"] = "".join(dd.xpath('./a/div/div[4]/text()').extract()[1]).strip()

            print(film)
            yield film

        # yield scrapy.Request(self.start_urls, callback=self.parse)