# 单元测试代码（使用Python内置的unittest框架）
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    # 测试加法
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    # 测试减法
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
    
    # 测试乘法
    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)
        self.assertEqual(multiply(-2, 3), -6)
    
    # 测试除法
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # 测试除数为0的异常
        with self.assertRaises(ValueError):
            divide(8, 0)

# 执行测试
if __name__ == '__main__':
    unittest.main()
