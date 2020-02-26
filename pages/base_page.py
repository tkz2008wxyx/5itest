from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings


class BasePage(object):
    def __init__(self,driver):
        self._driver = driver

    #设置显式等待，获取元素
    def find_element(self,*locator,timeout=None):
        try:
            return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        except (NoSuchElementException,TimeoutException):
            # self._driver.quit()
            raise TimeoutException(msg="定位元素失败，方法为{}".format(locator))

    def send_keys(self,webElement,keys):
        webElement.clear()
        webElement.send_keys(keys)

    def _init_wait(self,timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver,timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver,timeout=timeout)