# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import re

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


def to_float(value):
    return float(value.replace("kr. ", "").replace(",", "."))


def to_int(value):
    return int(value.replace("sider", "").strip())


class StringNumPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Clean and convert raw values
        f_price = to_float(adapter.get("price"))
        f_member_price = to_float(adapter.get("member_price"))
        i_pages = to_int(adapter.get("pages"))

        # Updates item fields
        adapter["price"] = f_price
        adapter["member_price"] = f_member_price
        adapter["pages"] = i_pages
        return item


class ValidPubPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Checks for valid publication date format
        if re.match(r"^\d{2}-\d{2}-\d{4}$", adapter.get("publication_date")):
            return item
        else:
            raise DropItem(f"Invalid publication data in {item}")


class CheckFieldsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Check if all fields are valid
        if not adapter.get("price"):
            raise DropItem(f"Missing price in {item}")
        elif not adapter.get("member_price"):
            raise DropItem(f"Missing member_price in {item}")
        elif not adapter.get("book_name"):
            raise DropItem(f"Missing book_name in {item}")
        elif not adapter.get("author_name"):
            raise DropItem(f"Missing author_name in {item}")
        elif not adapter.get("book_format"):
            raise DropItem(f"Missing book_format in {item}")
        elif not adapter.get("pages"):
            raise DropItem(f"Missing pages in {item}")
        elif not adapter.get("publication_date"):
            raise DropItem(f"Missing publication_date in {item}")

        else:
            return item
