import sys
import unittest
import os

class MainTester(unittest.TestCase):
    def test_imports(self) -> None:
        rtn = os.system("test_cmd")
        self.assertEqual(0, rtn)


if __name__ == "__main__":
    unittest.main()
