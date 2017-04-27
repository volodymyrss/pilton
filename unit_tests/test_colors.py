import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        import bcolors
        print bcolors.render("{RED}RED!{/}")

if __name__ == '__main__':
    unittest.main()
