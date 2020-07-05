import scrapy


class MaoyanItem(scrapy.Item):
    # 电影名称、电影类型和上映时间
    film_name = scrapy.Field()
    film_type = scrapy.Field()
    film_date = scrapy.Field()
