from setuptools import setup, find_packages

setup(
    license="MIT",
    name="dankware",
    version="3.6.8",
    author="SirDank",
    author_email="SirDankenstein@protonmail.com",
    description="Python package with various features!",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SirDank/dankware",
    project_urls={
        "GitHub": "https://github.com/SirDank/dankware",
        "Bug Tracker": "https://github.com/SirDank/dankware/issues",
    },
    keywords=[
        "dank",
        "dankware",
        "multithread",
        "gradient",
        "fade",
        "registry key",
        "error traceback",
        "random ip",
        "github scraper",
        "splash screen",
        "windows tools",
        "terminal",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development",
    ],
    package_dir={"": "."},
    packages=find_packages(where="."),
    extras_require={"extras": ["pillow"]},
    install_requires=[
        "rich",
        "colorama",
        "requests",
    ],
)
