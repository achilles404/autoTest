# coding=utf-8
import time
import unittest

# 测试类必须要继承TestCase类
class TestSample(unittest.TestCase):
    #类共享的fixture，在整个测试类执行过程中仅仅执行一次，需加装饰器@classmethod
    @classmethod
    def setUpClass(cls):
        print('整个测试类只执行一次 -- Start')

    #测试用例fixture
    def setUp(self):
        print('每个测试开始前执行一次')
    # 测试用例默认以test开头
    def test_equal(self):
        self.assertEqual(1, 1)
        time.sleep(3)
    def test_not_equal(self):
        self.assertNotEqual(1, 0)

    #测试用例fixture
    def tearDown(self):
        print('每个测试结束后执行一次')

    #类共享的fixture，在整个测试类执行过程中仅仅执行一次，需加装饰器@classmethod
    @classmethod
    def tearDownClass(cls):
        print('整个测试类只执行一次 -- End')

if __name__ == '__main__':
    unittest.main()