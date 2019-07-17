#! /usr/bin/env python
#coding=utf-8

import win32api  
import win32con  

keyname=u'Software\Microsoft\Internet Explorer\Main'  
page = u"www.linuxidc.net"
title = u'I love sina web site!'  
search_page = u'http://www.linuxidc.com'  

key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)  
win32api.RegSetValueEx(key, "Start Page", 0, win32con.REG_SZ, page)
win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)  
win32api.RegSetValueEx(key, 'Search Page', 0, win32con.REG_SZ, search_page)  
