#! /usr/bin/env python
#coding=utf-8
#mysetup.py

from distutils.core import setup
import py2exe

setup(console=["thread1.py"])

#usage:python mysetup.py py2exe