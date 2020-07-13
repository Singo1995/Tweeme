#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:11:00 2020

@author: arjun-singh
"""

class LemonMixin:
    def tastes_like(self):
        return super(LemonMixin, self).tastes_good() + ' and lemon'

class Cola:
    def tastes_like(self):
        return 'sugar'
    def tastes_good(self):
        return 'vodka'

class Coke:
    def tastes_like(self):
        return 'EEnipu'
    def tastes_good(self):
        return super(Coke, self).tastes_good() +' saraku'

class ColaLemon(LemonMixin, Coke , Cola):
    pass

drink = ColaLemon()
drink.tastes_like()
#drink = LemonMixin()
#print(drink.tastes_like())