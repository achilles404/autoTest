# coding=utf-8
import importlib.util
import os
import unittest


# 解析tests文件夹，并且返回module的字符串列表
def get_module_name_string(file_dir):
    # 要返回的用例列表
    return_list = []

    for root, dirs, file in os.walk(file_dir):
        for i in file:
            if not (i.endswith('__init__.py') or i.endswith('.pyc')) and i.startswith('test'):
                f = os.path.join(root, i)

                # // 以下为Windows用法，如Mac系统，需要改成：
                mod = 'tests.' + f.split('tests')[1].replace('.py', '').replace('/', '')
                # mod = 'tests.' + f.split('\\tests\\')[1].replace('.py', '').replace('\\', '.')
                return_list.append(mod)

    return return_list


if __name__ == "__main__":
    # # 定义suites
    # suites = unittest.TestSuite()
    #
    # # 获取所有的module的string，类似package.mod的方式
    # mod_string_list = (get_module_name_string(os.path.join(os.path.dirname(__file__), 'tests')))
    #
    # # 遍历每个mod string，import并且把它加入test case中来
    # for mod_string in mod_string_list:
    #     m = importlib.import_module(mod_string)
    #     test_case = unittest.TestLoader().loadTestsFromModule(m)
    #     suites.addTests(test_case)
    loader = unittest.defaultTestLoader
    # 生成测试用suite
    suite = loader.discover(os.path.join(os.path.dirname(__file__), 'tests'), top_level_dir=os.path.dirname(__file__))
    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)

    # 运行suites
    runner.run(suite)
