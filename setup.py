from distutils.core import setup

setup(
        name='pilton',
        version='1.0.1',
        py_modules= ['pilton','bcolors'],
        package_data     = {
            "": [
                "*.txt",
                "*.md",
                "*.rst",
                "*.py"
                ]
            },
        license='Creative Commons Attribution-Noncommercial-Share Alike license',
        long_description=open('README.md').read(),
        )
