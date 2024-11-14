# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""


def function(s):
    a = ""

    for i in s:
        if i in "([{":
            a = i
        elif i in ")]}:" and a == {"[": "]", "(": ")", "{": "}"}.get(i, None):
            pass
        else:
            return False
    return True


s1 = "(abcd)"
s2 = "(a)[{b}]{cd}"
s3 = "a[b(c]d)"

print(function(s1))
print(function(s2))
print(function(s3))
