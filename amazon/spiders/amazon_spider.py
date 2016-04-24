import scrapy
import re
from scrapy.selector import Selector
from amazon.items import AmazonItem



from scrapy_splash import SplashRequest


class AmazonSpider(scrapy.Spider):
	name = "amazon"
	allowed_domains = ["amazon.com"]

	start_urls = [
		#"file:///Users/zhenkangzhao15mbp/Documents/GitHub/Python/amazon/amazon_deal_render.html"
		#"http://www.amazon.com/gp/goldbox/ref=nav_cs_gb?nocache=1461265891556",
		"http://deals.ebay.com"
		#"http://www.amazon.com/gp/goldbox/ref=br_dig_smr?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-unrec-sidekick&pf_rd_r=06EPXD0QM51RQSKW5443&pf_rd_t=36701&pf_rd_p=83dc7404-b4a7-4852-9787-5348b3f9cf05&pf_rd_i=desktop-unrec"
	]

	def parse(self, response):



		imgs = response.xpath('//div[@class="slashui-image-cntr"]//img/@src').extract()

		print imgs

		deses = response.xpath('//div[@class="slashui-image-cntr"]//img/@alt').extract()


		print deses

		txts = response.xpath('//span[@class="first"]/text()').extract()


		print txts



		# for url in self.start_urls:
		# url = self.start_urls[0]
		# yield SplashRequest(
		# 	url,
		# 	self.parse_link,
		# 	endpoint='render.html',
		# 	args={
		# 		#'har': 1,
		# 		'html': 1,
		# 		'wait': 5,
		# 	}
		# )



#	def parse_link(self, response):


		# n = 0

		# while n < 16:
		# 	img = imgs[n]
		# 	print img
		# 	des = deses[n]
		# 	print des
		# 	txt = txts[n]
		# 	print txt
		# 	n += 1










		# imgs = response.xpath('//div[@class="a-row layer"]/img/@data-a-hires').extract()

		# deses = response.xpath('//span[@class="a-size-base a-color-link dealTitleTwoLine restVisible singleCellTitle autoHeight"]/text()').extract()

		# txts = response.xpath('//span[@class="a-size-medium a-color-base inlineBlock unitLineHeight"]/text()').extract()



		# n = 0

		# while n < 16:
		# 	img = imgs[n]
		# 	print img
		# 	des = deses[n]
		# 	print des
		# 	txt = txts[n]
		# 	print txt
		# 	n += 1


