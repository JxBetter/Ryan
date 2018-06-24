import unittest
from Ryan import Ryan, Param, Required, Optional

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        s = {
            'k1': Required(int),
            'k2': Optional(str),
        }

        d = {
            'k1': 3,
            'k2': '22',
        }

        self.assertEqual(Ryan(s).validate(d), True)

    def test_2(self):
        s = {
            'k1': Optional(int),
            'k2': Optional(str),
        }

        d = {

        }

        self.assertEqual(Ryan(s).validate(d), True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()