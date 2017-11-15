from util.db import DB
from util.log import logger


def get_db_value(self, element_name, where_condition):
    db = DB()
    db_map = self.property['db_map'][element_name]
    value = db.get(key=db_map[0], table=db_map[1], where_condition=where_condition)[0]
    return str(value)


def compare_db(self, element_name, where_condition):
    element_page_value = self.get_value(element_name)
    if not element_page_value:
        element_page_value = self.get_text(element_name)
    element_db_value = self.get_db_value(element_name, where_condition)
    logger.debug("%s---%s---%s", element_name, element_page_value, element_db_value)
    return element_page_value == element_db_value


def compare_db_all(self, where_condition):
    result = 1
    for element_name in self.property['db_map']:
        result = result and self.compare_db(element_name, where_condition)
    return result