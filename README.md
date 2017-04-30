# 基于Redis的布隆过滤器

## 简介

* BloomFilterRedis:使用Redis的Bitmap作为位数组构建起来的可扩展的布隆过滤器，位数组的默认长度为2^23，哈希函数默认为八个。
* orange：Scrapy工程，以“橘子水”为出发点的爬取百度百科的爬虫，配置了基于BloomFilterRedis的过滤器。

关于Bitmap以及其它介绍详见我的博文[基于Redis的布隆过滤器的实现](http://blog.csdn.net/qq_30242609/article/details/71024458)

## 开发环境

* python 2.7.12
* Redis 3.2.8
* python-redis
* scrapy 1.3.3

## 使用方法

```
from BloomFilterRedis import BloomFilterRedis

bloomFilterRedis = BloomFilterRedis("bloom")
bloomFilterRedis.do_filter("one item to check")
```

## Scrapy中的使用方法

1. 将`BloomFilterRedis`和复制到工程文件夹下，将`BloomRedisDupeFilter.py`复制到与`settings.py`同一目录下。
2. 在settings.py中配置以下字段：
  ```
  # 配置过滤器为基于redis的布隆过滤器
  DUPEFILTER_CLASS = 'orange.BloomRedisDupeFilter.BloomRedisDupeFilter'
  # reids中bitmap的key，默认为‘bloom’
  # BLOOM_REDIS_KEY = 'bloom'
  # redis的连接配置，默认为本机
  # BLOOM_REDIS_HOST = '127.0.0.1'
  # BLOOM_REDIS_PORT = 6379
  # 布隆过滤器的哈希列表，默认为8个，定义在GeneralHashFunctions中
  # BLOOM_HASH_LIST = ["rs_hash", "js_hash", "pjw_hash", "elf_hash", "bkdr_hash", "sdbm_hash", "djb_hash", "dek_hash"]
  ```

