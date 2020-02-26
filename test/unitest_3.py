import HTMLTestRunner
import os
import unittest

from config_ele import pro_root_path


class Exam(unittest.TestCase):
    i = 4

    def setUp(self) -> None:
        Exam.i += 3
        print('behind condition')
        print(Exam.i)

    def tearDown(self) -> None:
        Exam.i += 5
        print('after condition')
        print(Exam.i)

    def test_001(self):
        print('you are a batman')
        print(Exam.i)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Exam('test_001'))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    file_path = os.path.join(pro_root_path+'/report/first_case.html')
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='this is first report', description=u'这个是我们的第一次测试报告')
        runner.run(suite)

    print(Exam.i)