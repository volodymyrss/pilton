import unittest

import re

class TestStringMethods(unittest.TestCase):

    def test_import(self):
        import pilton

    def test_log(self):
        import pilton
        pilton.log("info log")
        pilton.logger.setLevel(pilton.logging.INFO)

    def test_print(self):
        import pilton
        pt=pilton.heatool("converttime")
        pilton.log(pt)

    def test_run(self):
        import pilton
        import os

        CFITSIO_INCLUDE_FILES = os.environ['CFITSIO_INCLUDE_FILES']
        print(("CFITSIO_INCLUDE_FILES before",CFITSIO_INCLUDE_FILES))

        pt=pilton.heatool("converttime")
        pt['informat']="IJD"
        pt['intime']="3000"
        pt['outformat'] = "UTC"
        pt.run()
        
        CFITSIO_INCLUDE_FILES = os.environ['CFITSIO_INCLUDE_FILES']
        print(("CFITSIO_INCLUDE_FILES after",CFITSIO_INCLUDE_FILES))


        self.assertFalse(re.search("2008-03-18T23:58:54.815",pt.output) is None)


if __name__ == '__main__':
    unittest.main()
