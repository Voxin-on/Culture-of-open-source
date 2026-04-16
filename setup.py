from setuptools import setup, find_packages

setup(
    name="vectors-calc",
    version="0.1.0",
    description="Simple vector operations: addition and scalar product",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)