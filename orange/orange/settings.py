# -*- coding: utf-8 -*-

BOT_NAME = 'orange'

SPIDER_MODULES = ['orange.spiders']
NEWSPIDER_MODULE = 'orange.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
}

ITEM_PIPELINES = {
    'orange.pipelines.OrangePipeline': 301,
}

# 配置过滤器为基于redis的布隆过滤器
DUPEFILTER_CLASS = 'orange.BloomRedisDupeFilter.BloomRedisDupeFilter'
# reids中bitmap的key，默认为‘bloom’
# BLOOM_REDIS_KEY = 'bloom'
# redis的连接配置，默认为本机
# BLOOM_REDIS_HOST = '127.0.0.1'
# BLOOM_REDIS_PORT = 6379
# 布隆过滤器的哈希列表，默认为8个，定义在GeneralHashFunctions中
# BLOOM_HASH_LIST = ["rs_hash", "js_hash", "pjw_hash", "elf_hash", "bkdr_hash", "sdbm_hash", "djb_hash", "dek_hash"]

# 设置为爬取策略广度优先
DEPTH_PRIORITY = 1

# 设置下载延迟
DOWNLOAD_DELAY = 5