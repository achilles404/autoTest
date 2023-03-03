# test_to_run.py
# coding=utf-8
import json
import unittest

flag = 'P0'
with open('./config/env_info', 'r', encoding='utf-8') as fp:
    result = json.load(fp)
    # 获取用例级别
    flag = result.get('level')


# flag = 'P0'
class TestToRun(unittest.TestCase):

    def setUp(self):
        pass
        # 这里写setUp的方法，通常是打开浏览器

    @unittest.expectedFailure
    def testAssertNotEqual(self):
        self.assertEqual(1, 2)
        # 这里写具体的search方法

    @unittest.skipUnless(flag == 'P1' or flag == 'P2', "P1级别用例")
    def testAssertEqual(self):
        self.assertEqual(1, 1)
        print("P1级别用例")
        # 这里写具体的search方法

    @unittest.skipUnless(flag == 'P2', "P2级别用例")
    def testAssertEqual2(self):
        self.assertEqual(1, 1)
        print("P2级别用例全部执行")
        # 这里写具体的search方法

    def tearDown(self):
        pass
        # tearDown方法，测试后的清理工具，比如对测试产生的数据进
