import unittest
from tdd import solution
class Testsolution(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(solution(10,20,"+"), 30)

    def test_multiplication(self):
        self.assertTrue(solution(10,20,"*"), 200)

    def test_subtraction(self):
        self.assertTrue(solution(10,20,"-"), -10)

    def test_division(self):
        self.assertTrue(solution(10,20.0,"/"), 0.5)    

if __name__=="__main__":
    unittest.main()
