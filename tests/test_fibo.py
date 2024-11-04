from unittest import TestCase
from lbdsa import fibo

class TestFibo(TestCase):
    def test_get_fibo_at(self):
        n = 19
        self.assertEqual(4181, fibo.fibo(n))

    def test_loop_and_recursion_same_result(self):
        n = 30
        memory = {}
        result_loop = fibo._fibo_using_loop(n, memory)
        result_recursion = fibo._fibo_using_recursion(n, memory)
        self.assertEqual(result_loop, result_recursion)
    
    def test_fibo_array_generated(self):
        memory = {}
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        actual = [fibo._fibo_using_recursion(n, memory) for n in range(len(expected))]
        self.assertEqual(expected, actual)
