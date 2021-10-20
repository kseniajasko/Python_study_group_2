import unittest

from task import linear_shift, circular_shift, nested_parentheses

class TestTask(unittest.TestCase):
    def test_linear_shift(self):
        start_array = [1, 2, 3, 4]
        shift = 3
        final_array = [0, 0, 0, 1]
        result_linear_shift = linear_shift(start_array, shift)
        self.assertEqual(result_linear_shift, final_array)

    def test_circular_shift_error(self):
        start_array = [1, 2, 3, 4]
        shift = 3
        final_array = [2, 3, 4, 1]
        result_circular_shift = circular_shift(start_array, shift)
        self.assertEqual(result_circular_shift, final_array)

    # def test_circular_shift_error(self):
    #     start_array = [1, 2, 3, 4]
    #     shift = 3
    #     final_array = [4, 3, 1, 2]
    #     result_circular_shift = circular_shift(start_array, shift)
    #     self.assertEqual(result_circular_shift, final_array)

    def test_nested_parentheses(self):
        incoming_1 = "((())(())())"
        incoming_2 = ""
        incoming_3 = "(((())))"
        incoming_4 = "())"
        incoming_5 = "(()()(())"
        self.assertTrue(nested_parentheses(incoming_1))
        self.assertTrue(nested_parentheses(incoming_2))
        self.assertTrue(nested_parentheses(incoming_3))
        self.assertFalse(nested_parentheses(incoming_4))
        self.assertFalse(nested_parentheses(incoming_5))



if __name__ == '__main__':
    unittest.main()