# -*- coding: utf-8 -*-


class OrangePipeline(object):

    def process_item(self, item, spider):
        with open("items.txt", "a") as f:
            f.write(str(item).decode("unicode_escape").encode('utf-8') + '\n')
        return item
