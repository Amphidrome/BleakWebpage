from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    name="bleak_webpage",
    version=__version__,
    description="Bleak Jellyfish Webpage",
    author="Bleak",
    author_email="bleak.jellyfish@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=0.10.0",
        "Flask-Webpack>=0.0.7"
    ]
)
