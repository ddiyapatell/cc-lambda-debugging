import unittest
from lambda_function3 import lambda_handler

class TestLambdaFunction3(unittest.TestCase):
    def test_evaluator1(self):
        result = lambda_handler({"expression": "2 1 +"})
        self.assertEqual(result['body'], 3)
    
    def test_evaluator_return(self):
        result = lambda_handler({"expression": "2 1 +"})
        self.assertEqual(result, {"statusCode": 200, "body": 3})

    def test_evaluator2(self):
        result = lambda_handler({"expression": "4 4 / 8 8 / +"})
        self.assertEqual(result['body'], 2)

    def test_evaluator3(self):
        result = lambda_handler({"expression": "5 10 * 5 10 / +"})
        self.assertEqual(result['body'], 50.5)

    def test_evaluator4(self):
        result = lambda_handler({"expression": "100 200 + 3 /"})
        self.assertEqual(result['body'], 100)
    

if __name__ == '__main__':
    unittest.main()