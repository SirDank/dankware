@echo off
title dankware

rmdir /s dist
mkdir dist
py311 -m build
echo.
py311 -m twine upload dist/*
pause