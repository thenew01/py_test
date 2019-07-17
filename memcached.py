#! /usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
import memcache

pymem = memcache.Client(['127.0.0.1:11211'],debug=0)
pymem.set("key5","hello,memcache!")
value = pymem.get("key5")
print value
