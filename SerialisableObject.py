# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:22:52 2014

@author: User
"""

class Task:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def PrintVals(self):
        print self.x, self.y
        
    def Calculate(self):
        return self.x * self.y
        