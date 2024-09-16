import unittest
import sys
from pathlib import Path

# local imports
sys.path.append(".")
# example: from src.main import main

ROOT = Path.cwd()


class TestFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test(self):
        self.assertEqual(None, None)


if __name__ == "__main__":
    unittest.main()
