# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 12:35:54 2012

@author: n3wp0llut10n
"""

mat = [
range(1,10),
range(1,10),
range(1,10),
range(1,10),
range(1,10),
range(1,10),
range(1,10),
range(1,10),
range(1,10)
]
      
res = 0
temp = 0

#check up-down
for i in range(len(mat[0])):
    for j in range(len(mat[0])):
            if j < (len(mat[0])-3):
                temp = mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
                res = max(temp, res)
    
            else:
                temp = mat[i][j]*mat[i][j-1]*mat[i][j-2]*mat[i][j-3]
                res = max(temp, res)
                
#check left-right
for j in range(len(mat[0])):
    for i in range(len(mat[0])):
            if i < (len(mat[0])-3):
                temp = mat[i][j]*mat[i+1][j]*mat[i+2][j]*mat[i+3][j]
                res = max(temp, res)
    
            else:
                temp = mat[i][j]*mat[i-1][j]*mat[i-2][j]*mat[i-3][j]
                res = max(temp, res)
            
#check left->right diagonal

print(res)
