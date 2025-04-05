from setuptools import setup

setup(
    name="api_testing",
    version="0.1",
    packages=[],  # Not needed since we're not making installable package
    install_requires=[
        "requests>=2.31.0",
        "pytest>=7.4.0",
        "pytest-xdist>=3.6.1",
        "pytest-mock>=3.14.0",
        "Faker>=19.13.0",
    ],
)
