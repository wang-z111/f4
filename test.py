import unittest
from f4 import *
class test(unittest.TestCase):

    def test_f4(self):
        pass
    def test_f4_answer(self):
        print("单元测试开始：")
        _eq = input("请输入一个四则运算：")
        _eq_ans = input("请输入一个正确的答案：")
        self.assertEqual(_eq_ans ,f4()._f4_answer(eq = _eq))
        print("单元测试结束。")
    def test_f4_input(self):
        print("单元测试开始：")
        self.assertEqual(0,f4()._f4_input())
        print("单元测试结束。")
    def test_f4_integer_parser(self):
        print("单元测试开始：")
        x = input("请输入命令行参数：")
        self.assertEqual(0,f4()._f4_integer_parser(x))
        print("单元测试结束。")
if __name__ == '__main__':
    unittest.main()
