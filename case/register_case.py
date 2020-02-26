#coding=utf-8

import HTMLTestRunner
import os
import time
import unittest
from selenium import webdriver
from business.register_business import RegisterBusiness
from config_ele import pro_root_path
from log.user_log import UserLog


class RegisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = UserLog()
        cls.logger = cls.log.get_logger()

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.logger.info('this is firefox')
        self.register = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        # self.driver.save_screenshot(r'F:\Python\5itest_po_3\report\11.png')
        #当使用HTMLtestrunner模式运行，不会进行打印操作,但是函数依旧会运行
        # print('==============')
        # print(self.__dir__())
        #截图是可以配合断言一起使用的，当断言失败，即case执行异常，也会截图
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path_1 = os.path.join(pro_root_path + '/report/' + case_name + '.png')
                print(file_path_1)
                self.driver.save_screenshot(file_path_1)
        self.driver.close()
        print("这是case的后置条件")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close_logger()

    def test_email_error(self):
        self.register.user_base('34abc','aaasdf','111111','asd2f')
        email_error = self.register.get_user_text('user_email_error')
        if email_error is None:
            flag = True
        else:
            flag = False
        self.assertFalse(flag,'case执行失败')

    def test_username_error(self):
        pass

    def test_password_error(self):
        pass

    def test_code_error(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RegisterCase('test_email_error'))
    # suite.addTest(RegisterCase('test_username_error'))
    # suite.addTest(RegisterCase('test_password_error'))
    # suite.addTest(RegisterCase('test_code_error'))
    # suite.addTest(RegisterCase('test_success'))

    file_path = os.path.join(pro_root_path+'/report/first_case.html')
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='this is first report', description=u'这个是我们的第一次测试报告')
        runner.run(suite)

    # runner = unittest.TextTestRunner()
    # runner.run(suite)