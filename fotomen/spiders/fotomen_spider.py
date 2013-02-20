from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from fotomen.items import FotomenItem

class FotomenSpider(BaseSpider):
	name = "fotomen"
	allowed_domains = ["fotomen.cn"]
	start_urls = ["http://fotomen.cn/category/appreciation/"]

	def parse(seld, response):
		hxs = HtmlXPathSelector(response)
		pages = hxs.select("//div[@class='post_thumbnail']/a")
		items = []
		for page in pages:
			item = FotomenItem()
			item['title'] = page.select("h2/text()").extract()
			item['link'] = page.select("@href").extract()

			print item['title'], item['link']
			items.append(item)
		return items


