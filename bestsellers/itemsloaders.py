import re

from itemloaders.processors import Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class BookLoader(ItemLoader):
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()
    author_name_out = Join(separator="/")
    date_in = MapCompose()
