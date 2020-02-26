import unittest


class Exam(unittest.TestCase):
    def setUp(self) -> None:
        print('behind condition')

    def tearDown(self) -> None:
        print('after condition')

    def test_001(self):
        print('you are a batman')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Exam('test_001'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)