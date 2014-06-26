#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nikeah
#
# Created:     16/06/2014
# Copyright:   (c) Nikeah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class SerialisableTestClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def Calculate(self):
        return self.arg1 * self.arg2