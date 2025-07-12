from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI Model",
    version="0.1",
    author="Sachin Verma",
    packages=find_packages(),
    install_requires = requirements,
)