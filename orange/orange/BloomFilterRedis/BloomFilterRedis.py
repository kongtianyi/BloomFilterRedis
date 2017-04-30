# -*- coding: utf-8 -*-

import redis
import GeneralHashFunctions


class BloomFilterRedis:

    hash_list = ["rs_hash", "js_hash", "pjw_hash", "elf_hash", "bkdr_hash",
                 "sdbm_hash", "djb_hash", "dek_hash"]

    def __init__(self, key, host='172.0.0.1', port=6379, hash_list=hash_list):
        # redis-bitmap的key
        self.key = key
        # redis连接信息
        self.pool = redis.ConnectionPool(host=host, port=port)
        self.handle = redis.StrictRedis(connection_pool=self.pool, charset='utf-8')
        # 哈希函数列表
        self.hash_list = hash_list

    @classmethod
    def random_generator(cls, hash_value):
        '''
        将hash函数得出的函数值映射到[0, 2^32-1]区间内
        '''
        return hash_value % (1 << 32)

    def do_filter(self, item):
        '''
        检查是否是新的条目，是新条目则更新bitmap并返回True，是重复条目则返回False
        '''
        flag = False
        for hash_func_str in self.hash_list:
            # 获得到hash函数对象
            hash_func = getattr(GeneralHashFunctions, hash_func_str)
            # 计算hash值
            hash_value = hash_func(item)
            # 将hash值映射到[0, 2^32]区间
            real_value = BloomFilterRedis.random_generator(hash_value)
            # bitmap中对应位是0，则置为1，并说明此条目为新的条目
            if self.handle.getbit(self.key, real_value) == 0:
                self.handle.setbit(self.key, real_value, 1)
                flag = True
        # 当所有hash值在bitmap中对应位都是1，说明此条目重复，返回False
        return flag
