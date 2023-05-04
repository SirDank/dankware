from setuptools import setup, find_packages

setup(

    license = "MIT",
    name = "dankware",
    version = "3.3.7",
    author = "SirDank",
    
    author_email = "SirDankenstein@protonmail.com",
    description = "Python package with various features!",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/SirDank/dankware",

    project_urls = {
        "GitHub": "https://github.com/SirDank/dankware",
        "Bug Tracker": "https://github.com/SirDank/dankware/issues",
    },

    keywords = [
        "dank",
        "dankware",
        "multithread",
        "gradient",
        "fade",
        "registry key",
        "error traceback",
        "random ip generator",
        "github scraper",
        "splash screen",
        "hide window",
        "file selector",
    ],

    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development",
    ],

    package_dir = {"": "."},
    packages = find_packages(where = "."),
    install_requires = [
        "rich",
        "colorama",
        "requests",
        "pillow",
    ],
)