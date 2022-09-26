import codecs
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.5'
DESCRIPTION = 'A JWT auth library based on Django and strawberry'
# Setting up
setup(
    name="strawberry_jwt_auth",
    version=VERSION,
    author="grvsh02 (Gaurav Sharma)",
    author_email="<gaurav021201@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyjwt', 'strawberry-graphql', 'django', 'phonenumbers'],
    keywords=['python', 'jwt', 'auth', 'strawberry', 'graphql', 'Authentication'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)