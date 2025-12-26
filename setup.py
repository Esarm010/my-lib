from setuptools import setup, find_packages

setup(
    name="my-lib-arman",          # СДЕЛАЙ УНИКАЛЬНОЕ имя (например с ником)
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={"my_lib": ["data/*.txt"]},
)
