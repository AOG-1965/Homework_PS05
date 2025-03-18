import scrapy


class LightingnewparsSpider(scrapy.Spider):
    name = "lightingnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        light_devices = response.css('div.WdR1o')
        for light_device in light_devices:
            yield {
                'name': light_device.css('div.lsooF span::text').get(),
                'price': light_device.css('div.pY3d2 span::text').get(),
                'url': light_device.css('a').attrib['href']
            }
