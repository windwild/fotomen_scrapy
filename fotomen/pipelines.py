# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class FotomenPipeline(object):
    def process_item(self, item, spider):
        ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
        IMAGES_STORE = '/Users/windwild/Code/project/fotomen/images'
        return item
