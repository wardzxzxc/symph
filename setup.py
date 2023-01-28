import os
import re

from setuptools import find_packages, setup

version = re.compile(r"VERSION\s*=\s*\((.*?)\)")


def get_requirements(filename):
    return open("requirements/" + filename).read().splitlines()


def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "flower/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return ".".join(m.groups()[0].split(", "))


setup(
    name="symph",
    version=get_package_version(),
    description="Symph",
    long_description=open("README.rst").read(),
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=get_requirements("default.txt"),
    entry_points={
        "celery.commands": [
            "flower = flower.command:flower",
        ],
    },
)
