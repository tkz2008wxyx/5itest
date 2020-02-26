import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        #创建对象，看起来像个容器，如果不往里面添加东西，这为空
        self.logger = logging.getLogger()
        #设置等级
        self.logger.setLevel(logging.DEBUG)
        #创建流对象，向控制台输出日志
        #console = logging.StreamHandler()
        #向logger中添加流对象
        #logger.addHandler(console)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        des_dir = os.path.join(base_dir,'logs')
        file_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        file_path = os.path.join(des_dir,file_name)
        # print(datetime.datetime.now().strftime('%Y-%m-%d'))
        # print(file_path)

        #创建流对象，向文件输出日志
        #默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
        #日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，
        #当然也可以自己定义日志级别。
        self.file_log = logging.FileHandler(file_path,'a',encoding='utf-8')
        self.file_log.setLevel(logging.DEBUG)
        format_style = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s')
        self.file_log.setFormatter(format_style)
        self.logger.addHandler(self.file_log)


    def get_logger(self):
        return self.logger

    def close_logger(self):
        self.logger.removeHandler(self.file_log)
        self.file_log.close()


if __name__ == '__main__':
    log = UserLog()
    logger = log.get_logger()
    #等级要高于或等于self.file_log.setLevel(logging.DEBUG)
    logger.debug('unitest')
    log.close_logger()


