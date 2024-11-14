# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""


def CHECK_POINT(desc, condictionResult):
    print(f'检查点{desc}')
    if condictionResult:
        print('通过')
    else:
        print('不通过')
        exit(2)
