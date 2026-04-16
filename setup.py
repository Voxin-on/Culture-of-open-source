from setuptools import setup, find_packages

setup(
    name="vectors-calc",
    version="0.1.2",
    description="Simple vector operations: addition and scalar product",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Voxin-on/Culture-of-open-source",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)