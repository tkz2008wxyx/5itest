#coding=utf-8
import configparser


class ReadIni():
    def __init__(self,file_path=None,node=None):
        if file_path is None:
            file_path = 'F:\Python\imooc_selenium_po\config\LocalElement.ini'
        if node is None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.read(file_path)

    #加载文件
    def read(self,file_path):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf

    #获取value值
    def get_value(self,key):
        result = self.cf.get(self.node,key)
        return result


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('user_email_error'))


# cf = configparser.ConfigParser()
# cf.read('F:/Python/imooc_selenium/config/LocalElement.ini')
# print(cf.get('RegisterElement','user_email'))