from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = '0.1.0'
DESCRIPTION = 'A JWT auth library based on Django and strawberry'
# Setting up
setup(
    name="strawberry-jwt-auth",
    version=VERSION,
    author="grvsh02 (Gaurav Sharma)",
    author_email="<gaurav021201@gmail.com>",
    description=DESCRIPTION,
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