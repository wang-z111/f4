import unittest
from f4 import *
class test(unittest.TestCase):
    #测试功能1、功能2

    def test_f4(self):
        pass
    def test_f4_answer(self):
        print("_f4_answer函数单元测试开始：")
        _eq = input("输入一个四则运算：")
        _eq_ans = input("输入一个正确的答案：")
        self.assertEqual(_eq_ans ,f4()._f4_answer(eq = _eq))
        print("_f4_answer函数单元测试结束。")
        print("OK")
    def test_f4_input(self):
        print("_f4_input函数单元测试开始：")
        self.assertEqual(0,f4()._f4_input())
        print("_f4_input函数单元测试结束。")
        print("OK")
    def test_f4_integer_parser(self):
        print("_f4_integer_parser函数单元测试开始：")
        x = input("输入命令行参数：")
        self.assertEqual(0,f4()._f4_integer_parser(x))
        print("_f4_integer_parser函数单元测试结束。")
        print("OK")
if __name__ == '__main__':
    unittest.main()
