#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ = = '__main__':
    n = int(input("Сколько вы купили карандашей? "))    
    if n <= 0 or n > 10:    
        print("Вы ввели некорректное число!")   
    elif 1 < n < 5: 
        print("Я купил", n, "карандаша")    
    elif n == 1:
        print("Я купил", n, "карандаш") 
    else:   
        print("Я купил", n, "карандашей")  
