from setuptools import setup, find_packages

setup(
  name="dankware",
  version="3.2.1",
  author="SirDank",
  author_email="SirDankenstein@protonmail.com",
  description="Python module with various features.",
  long_description=open("README.md","r",encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/SirDank/dankware",
  project_urls={
    "GitHub": "https://github.com/SirDank/dankware",
    "Bug Tracker": "https://github.com/SirDank/dankware/issues",
  },
  license="MIT",
  keywords=["dank","dankware","multithread","gradient","fade","registry key","error traceback","random ip","github scraper"],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Natural Language :: English",
  "Topic :: Software Development"
  ],
  package_dir={"": "."},
  packages=find_packages(where="."),
  install_requires=['rich', 'colorama', 'requests']
)