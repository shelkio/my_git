# _*_ coding: utf-8 _*_
from framework.base_page import BasePage

class HomePage(BasePage):


    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    # 百度新闻入口
    news_link = u"link_text=>新闻"

    def type_search(self,text):
        self.type(self.input_box,text)
    def send_submit_btn(self):
        self.click(self.search_submit_btn)
    def get_title(self):
        return self.get_page_title()
    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)