# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 19:52:28 2022

@author: Juliano
"""
import os

ano = int(input('Informe o ano: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):

    print('Ano bissexto')

else:

    print('Ano não bissexto')
    
    os.system('pause')
    