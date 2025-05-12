from setuptools import setup, find_packages

setup(
    name="topstepapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "signalrcore"
    ],
    python_requires=">=3.7",
)