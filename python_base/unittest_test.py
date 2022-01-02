# unittest例子
import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('seltUp Class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDown Class')

    def setUp(self) -> None:
        print('seltUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_01(self):
        self.assertEqual(2, 2, '测试相等')
        print('test_01')
    # 跳过某条case
    @unittest.skipIf(1 + 1 == 2, '跳过')
    def test_02(self):
        self.assertEqual(1, 1, '测试相等')
        print('test_02')

    def test_03(self):
        self.assertEqual(3, 4, '测试相等')
        print('test_03')


class demo1(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, 1, '测试相等')
        print('demo1_test_01')

    def test_02(self):
        self.assertEqual(1, 1, '测试相等')
        print('demo1_test_02')

# 执行测试用例的方法
if __name__ == '__main__':
    # 方法1：unittest.main()用来运行全部的case
    # unittest.main()
    #
    # # 方法2：加入容器中执行
    # suite = unittest.TestSuite()
    # # 套件添加多个用例
    # suite.addTests([demo('test_01'), 12ProTesting('test_02')])
    # # 套件添加每次添加一个用例
    # suite.addTest(demo('test_01'))
    # suite.addTest(12ProTesting('test_02'))
    # unittest.TextTestRunner().run(suite)
    # 方法3：同时测试多个类
    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(12ProTesting)
    # suite_all = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suite_all)
    # 方法4：匹配某个目录下的文件，执行这些文件的所有测试用例
    discover = unittest.defaultTestLoader.discover('../', 'unittest_*.py')
    unittest.TextTestRunner().run(discover)
