#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = float(input("Введите число a "))
    b = float(input("Введите число b "))
    c = float(input("Введите число c "))
    if a > b and a > c:
        print("Максимальное ", a)
    elif b > c and b > a:
        print("Максимальное ", b)
    else:
        print("Максимальное ", c)
