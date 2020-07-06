
import re

def test_import():
    import pilton

def test_log():
    import pilton
    pilton.log("info log")
    pilton.logger.setLevel(pilton.logging.INFO)

def test_print():
    import pilton
    pt=pilton.heatool("converttime")
    pilton.log(pt)

def test_run():
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

    assert re.search("2008-03-18T23:58:54.815",pt.output) is not None


