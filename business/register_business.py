import time

from selenium.webdriver.common.by import By
from selenium import webdriver


from pages.base_page import BasePage


class RegisterBusiness(BasePage):
    # driver = webdriver.Chrome()
    # url = 'http://www.5itest.cn/register'
    email = (By.ID,'register_email')
    username = (By.ID,'register_nickname')
    password = (By.ID,'register_password')
    code_text = (By.ID,'captcha_code')
    register_button = (By.ID,'register-btn')

    email_error = (By.ID, 'register_email-error')
    username_error = (By.ID, 'register_nickname-error')
    password_error = (By.ID, 'register_password-error')
    code_text_error = (By.ID, 'captcha_code-error')

    # def __init__(self):
    #     super().__init__(self.driver,self.url)

    def user_base(self,email,username,password,code_text):
        self.send_keys(webElement=self.find_element(*self.email),keys=email)
        self.send_keys(webElement=self.find_element(*self.username),keys=username)
        self.send_keys(webElement=self.find_element(*self.password),keys=password)
        self.send_keys(webElement=self.find_element(*self.code_text),keys=code_text)
        self.click_register_button()
        time.sleep(3)

    # 获取文字信息
    def get_user_text(self, info):
        try:
            if info == 'user_email_error':
                # print(self.register_p.get_email_error_element().text)
                # print(self.register_p.get_email_error_element().get_attribute("value"))
                return self.find_element(*self.email_error).text
            elif info == 'user_name_error':
                return self.find_element(*self.username_error).text
            elif info == 'password_error':
                return self.find_element(*self.password_error).text
            else:
                return self.find_element(*self.code_text_error).text
        except:
            return None

    #点击注册按钮
    def click_register_button(self):
        self.find_element(*self.register_button).click()