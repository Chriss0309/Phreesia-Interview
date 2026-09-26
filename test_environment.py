import sys
import unittest


class EnvironmentTest(unittest.TestCase):
    def test_python_meets_interview_minimum(self):
        self.assertGreaterEqual(sys.version_info[:2], (3, 10))


if __name__ == "__main__":
    unittest.main()
