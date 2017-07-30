import unittest
import parser


class ParserTestSuite(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()

    def test_should_change_strings_into_numbers(self):
        line1 = "1,Abc,2\n"
        line2 = "Def,Def,4\n"
        line3 = "?,Abc,5\n"

        attributes = [
            {"attributes": [1.0, 0.0], "class": 2.0},
            {"attributes": [0.0, 1.0], "class": 4.0},
            {"attributes": ["?", 0.0], "class": 5.0}]

        self.assertEqual(self.parser.parse(line1+line2+line3), attributes)


if __name__ == "__main__":
    unittest.main()
