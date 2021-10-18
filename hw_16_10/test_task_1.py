import io
import unittest
from unittest.mock import patch, Mock

from task_1 import Matrix, SignedInt

class TestMatrix(unittest.TestCase):

    def test_matrix_object(self):
        numb = SignedInt(5, '+')
        self.assertEqual(numb.number(), 5)

if __name__ == '__main__':
    unittest.main()