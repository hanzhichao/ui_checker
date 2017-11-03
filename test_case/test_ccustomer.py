from time import sleep

from base import Base
from page.page_obj.customer.ccustomer import CCustomer


class TestCcustomer(Base):
    def test_search_customer(self):
        page = CCustomer(self.driver)
        page.login()
        page.load()
        page.search_phone('18010181267')
        sleep(10)
        self.driver.quit()
