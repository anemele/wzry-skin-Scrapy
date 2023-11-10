# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from pathlib import Path

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WzryPipeline:
    def process_item(self, item, spider):
        path: Path = item.get('path')
        if path is None:
            raise ValueError

        data = item.get('data')
        if data is None:
            raise ValueError

        path.write_bytes(data)

        return f'SAVE: {path}'
