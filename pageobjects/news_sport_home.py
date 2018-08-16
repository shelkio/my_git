# _*_ coding: utf-8 _*_
from framework.base_page import BasePage

class SprotsHomePage(BasePage):
    #汽车新闻入口
    car_link = "xpath=>//*[@id='channel-all']/div/ul/li[13]/a"
    def click_car(self):
        self.click(self.car_link)
        self.sleep(2)

