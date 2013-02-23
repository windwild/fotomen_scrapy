#coding=utf-8


from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


from fotomen.items import FotomenItem

class FotomenSpider(BaseSpider):
	name = "fotomen"
	allowed_domains = ["fotomen.cn"]
	start_urls = ["http://fotomen.cn/category/appreciation/"]
	#download_delay = 2
	posts_urls = []
	index_urls = []

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		pages = hxs.select("//div[@class='post_thumbnail']/a")

		for page in pages:
			page_url = page.select("@href").extract()[0]
			print "page:",page_url
			FotomenSpider.posts_urls.append(page_url)
			yield Request(page_url, callback=self.detail)

		for index_url in hxs.select("//a[@class='ajax_link']/@href").extract():
			if(index_url not in FotomenSpider.index_urls):
				print "index_url:",index_url
				FotomenSpider.index_urls.append(index_url)
				yield Request(index_url, callback=self.parse)

	def detail(self,response):
		title_file = open("title.txt","a")
		hxs = HtmlXPathSelector(response)
		title = hxs.select("//a[@class='readmore']/text()").extract()
		title = title[0].encode('utf8').strip()
		print "title:",title
		title_file.write("title:%s\n"%(title))
		title_file.close()
		item = FotomenItem()

		item['title'] = title

		item['url'] = response.url

		item['image_urls'] = hxs.select("//div[@id='content-pure']//img/@data-lazy-src").extract()

		yield item


