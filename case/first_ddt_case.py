#coding=utf-8

import sys
import ddt
import time

sys.path.append('F:\\Python\\5itest_po_3')

import unittest
import os
import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from config_ele import pro_root_path
from util.excel_util import ExcelUtil

ex = ExcelUtil(r'F:\Python\5itest_po_3\config\case_excel.xls')
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(self) -> None:
    #     self.file_image = r'F:\Python\imooc_selenium_po\image\test001.png'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.register = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path_1 = os.path.join(pro_root_path + '/report/' + case_name + '.png')
                self.driver.save_screenshot(file_path_1)
        self.driver.close()
        print("这是case的后置条件")

    # @ddt.data(
    #     ['12','tom15s','111111','F:\\Python\\imooc_selenium_po\\image\\test001.png','user_email_error','请输入有效的电子邮件地址'],
    #     ['@qq.com', 'tom15s', '111111', 'F:\\Python\\imooc_selenium_po\\image\\test001.png', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['1esse2@qq.com', 'tom15s', '111111', 'F:\\Python\\imooc_selenium_po\\image\\test001.png', 'user_email_error', '请输入有效的电子邮件地址']
    # )
    # @ddt.unpack

    @ddt.data(*data)
    def test_register(self,data):
        #特别注意:在Excel中不要出现多余的数据，否则解析数据时会出错
        email,user_name,password,code_text,assert_code = data
        self.register.user_base(email,user_name,password,code_text)
        email_error = self.register.get_user_text(assert_code)
        if email_error is None:
            flag = True
        else:
            flag = False
        self.assertFalse(flag, 'case执行失败')


if __name__ == '__main__':
    file_path = os.path.join(pro_root_path + '/report/ddt_case1.html')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='this is first report1', description=u'这个是我们的第一次测试报告1')
        runner.run(suite)