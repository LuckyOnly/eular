# coding:utf-8
import a66_Diophantine_equation,a66_others
import unittest

class unit(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        for i in range(5,14):
            try:
                self.assertEqual(a66_others.pell(i),a66_Diophantine_equation.GetMinx(i))
            except Exception as e:
                print e.message

if __name__ == '__main__':
    unittest.main()

