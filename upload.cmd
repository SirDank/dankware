@echo off
title dankware

rmdir /s dist
mkdir dist
py -m build
py -m twine upload dist/*
pause