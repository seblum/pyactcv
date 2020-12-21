from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'pandas',
    'numpy'
]

setup_requires = [
    'pytest-runner'
]

tests_require = [
    'pytest',
    'coverage==4.*',
    'pytest-cov',
    'coveralls'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyactcv",
    version="0.0.2",
    author="Sebastian Blum",
    author_email="sebast.blum@gmail.com",
    description="Combine the Cognitive Architecture ACT-R with user data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seblum/pyactcv",
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
