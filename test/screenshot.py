import time

from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.save_screenshot(r'F:\Python\5itest_po_3\report\11.png')
time.sleep(3)
print('success')
driver.close()