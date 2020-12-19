#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(6):
    if not (100 - 19 * i) % 9 :
        print('быков =', i)
        print('коров =', (100 - 19 * i) // 9)
        print('телят =', (100 - 10 * i - 5 * (100 - 19 * i) // 9) * 2)