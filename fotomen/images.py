from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request

import os
import time
import hashlib
import urlparse
import rfc822
from cStringIO import StringIO
from collections import defaultdict

from twisted.internet import defer, threads
from PIL import Image

from scrapy import log
from scrapy.utils.misc import md5sum
from scrapy.exceptions import DropItem, NotConfigured, IgnoreRequest
from scrapy.contrib.pipeline.media import MediaPipeline


class MyImagesPipeline(ImagesPipeline):
    title = "default"

    def image_key(self, url):
        year,month = url.split('/')[-3],url.split('/')[-2]
        image_guid = hashlib.sha1(url).hexdigest()
        img_path = "%s/%s/%s" % (year,month,self.title)
        return '%s/%s.jpg' % (img_path, image_guid)

    def get_media_requests(self, item, info):
        self.title = item['url'].split('/')[-2]
        for image_url in item['image_urls']:
            yield Request(image_url)
