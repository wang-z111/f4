# by: psy_yp
class f4(object):
    def __init__(self):  # 初始化新建对象
        pass

    """
  功能1、2：实现含有括号的四则运算
"""

    def _f4(self):
        from random import randint as r  # 直接导入randint函数,更名为r
        from random import uniform as ru  # 直接导入uniform函数,更名为ru,用于生成指定范围内的随机浮点数
        from fractions import Fraction as f  # 直接导入fractions函数,更名为f
        ops = ['+', '-', '*', '/']  # 存储操作符
        kuohao = ['(', '', ')']  # 存储括号，下标为0,1,2

        left1 = r(0, 1)
        left2 = r(0, 1)
        left3 = r(0, 1)
        right1 = r(1, 2)
        right2 = r(1, 2)
        right3 = r(1, 2)
        if left1 == 0:
            left2 = 1
            left3 = 1
            if right1 == 2:
                right2 = 1
                right3 = 1
            else:
                right2 = 2
                right3 = 1
        else:
            if left2 == 0:
                left3 = 1
                right1 = 1
                if right2 == 2:
                    right3 = 1
                else:
                    right3 = 2
            else:
                left3 = 0
                right1 = 1
                right2 = 1
                right3 = 2
        add_1 = ru(0, 1)
        add_1 = f(add_1).limit_denominator(10)  # 限制最大分母值,小数变分数
        add_2 = ru(0, 1)
        add_2 = f(add_2).limit_denominator(10)
        add_3 = r(1, 10)
        add_4 = r(1, 10)
        ops1 = r(0, 2)
        ops2 = r(0, 3)
        ops3 = r(0, 3)
        # 由上述操作，随机生成表达式
        eq = kuohao[left1] + str(add_1) + ops[ops1] + kuohao[left2] + str(add_2) + kuohao[right1] + ops[ops2] + kuohao[
            left3] + str(add_3) + kuohao[right2] + ops[ops3] + str(add_4) + kuohao[right3]
        return (eq)

    def _f4_answer(self, eq):
        from fractions import Fraction as f
        answer1 = f(eval(eq)).limit_denominator(1000)
        answer1 = str(answer1)
        return (answer1)

    def _f4_input(self):
        try:
            yes = 0
            no = 0
            for i in range(20):  # 输出20道题，分别判断输入结果与正确答案是否相同，按要求输出
                _eq = f4()._f4()
                print(_eq, "=")
                _ans_right = f4()._f4_answer(eq=_eq)
                _ans = input("?")
                if _ans == _ans_right:
                    print("答对啦，你真是个天才！")
                    yes = yes + 1
                else:
                    print("再想想吧，答案似乎是", _ans_right, "喔！")
                    no = no + 1
            print("你一共答对", yes, "道题，共20道题。")
        except:
            print("输入有误")
        return (0)

    """
功能3：限定题目数量，"精美"打印输出，避免重复
功能4：在功能3的基础上，支持分数出题和运算
"""

    def _f4_integer_parser(self, x):
        _p = "题目数量必须是  正整数。"
        try:
            x = int(x)
            if x >= 0:
                for i in range(x):
                    _eq = f4()._f4()
                    _right = f4()._f4_answer(eq=_eq)
                    _eq = _eq + "="
                    print(_eq.ljust(40), _right)  # 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
            else:
                print(_p)
        except:
            print(_p)
        return (0)


if __name__ == "__main__":
    import argparse  # argparse是一个{命令行参数解析}模块

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cin")
    args = parser.parse_args()
    if args.cin == None:
        f4()._f4_input()
    else:
        f4()._f4_integer_parser(args.cin)

# *************************************************


