# -*- coding: utf-8 -*-
"""
Created on Fri Nov 02 20:30:11 2012

@author: n3wp0llut10n
"""

res = 0
big_num = pow(2,1000)
big_str = str(big_num)
for i in range(0, len(big_str)):
    res += int(big_str[i])
    
print res