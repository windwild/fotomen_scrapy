# Scrapy settings for fotomen project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'fotomen'

SPIDER_MODULES = ['fotomen.spiders']
NEWSPIDER_MODULE = 'fotomen.spiders'

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = '/Users/windwild/Code/project/fotomen/images/'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fotomen (+http://www.yourdomain.com)'
