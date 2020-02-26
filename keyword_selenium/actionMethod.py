#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from util.excel_util import ExcelUtil
import time

class ActionMethod():
    def __init__(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.basepage = BasePage(self.driver)


    #输入URL
    def get_url(self,url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.page_source

    #获取元素
    def get_element(self,locator):
        try:
            element = self.basepage.find_element(*(By.ID,locator))
            return element
        except:
            return None

    #向元素输入值
    def element_send_key(self,locator,value):
        self.basepage.send_keys(webElement=self.get_element(locator),keys=value)

    #点击
    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    #等待
    def sleep_time(self):
        time.sleep(3)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()


if __name__ == '__main__':
    action_method = ActionMethod('firefox')
    action_method.get_url('https://www.baidu.com')
    action_method.driver.maximize_window()
    # input_frame = (By.ID,'kw')
    action_method.element_send_key('kw',value='5itest')
    # button = (By.ID, 'su')
    action_method.get_element('su').click()
    time.sleep(4)
    action_method.driver.close()
