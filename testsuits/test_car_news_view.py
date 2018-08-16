# _*_ coding: utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SprotsHomePage


class CarNewsView(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_car_news(self):
        #初始化百度页面，并点击新闻链接
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()
        #初始化新闻主页对象，并点击体育
        newshome = NewsHomePage(self.driver)
        newshome.click_sports()
        #初始化体育主页对象，并点击汽车
        sportnewhome = SprotsHomePage(self.driver)
        sportnewhome.click_car()
        sportnewhome.get_windows_img()

if __name__ == "__main__":
    unittest.main()
