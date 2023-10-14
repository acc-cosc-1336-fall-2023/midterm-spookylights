#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config,use_global,global_x
from src.question_b.question_b import is_prime
from src.question_c.question_c import get_bonus_pay
from src.question_d.question_d import use_local_variable



class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_use_global(self):
        self.assertEqual(global_x(), 0)
        use_global()
        self.assertEqual(global_x(), 100)
    
    def test_is_prime(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(11), True)

    def test_get_bonus_pay(self):
        self.assertEqual(get_bonus_pay(-1), "Invalid Arguments")
        self.assertEqual(get_bonus_pay(200), 10)
        self.assertEqual(get_bonus_pay(600), 36)
        self.assertEqual(get_bonus_pay(1000), 70)
        self.assertEqual(get_bonus_pay(1500), 120)
        self.assertEqual(get_bonus_pay(2000), "Invalid Arguments")

    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)


