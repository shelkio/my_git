# _*_ coding: utf-8 _*_
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_tiltle(self):

        homepage = HomePage(self.driver)
        print homepage.get_title()
        homepage.sleep(2)

if __name__ == "__main__":
    unittest.main()
