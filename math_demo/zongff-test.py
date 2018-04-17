# coding:utf-8
import unittest
from  a12_Highly_divisible_triangular_number import *
class unit(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):

        self.assertEqual(is_prime(10),False)
        self.assertEqual(is_prime(5), True)

    def test_02(self):
        self.assertEquals(construction_prime(1),[2])
        self.assertEquals(construction_prime(3), [2,3,5])

    def test_03(self):
        S=[2,3,1,1]
        self.assertEquals(index(S),6)

    def test_04(self):
        self.assertEquals(factors(3),[])
if __name__ == '__main__':
    unittest.main()