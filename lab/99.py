# -*- coding: utf-8 -*-
'''
Created on 2013-11-9

@author: young
'''
def V1_99(start,end):    
    seq=xrange(start,end+1)
    magicstring=''
    for i in seq:
        row=''
        for j in range(i):
            row=row+'%s*%s=%s\t'%(i,j+1,i*(j+1))        
        magicstring+=row+'\n'
    return magicstring


if __name__=='__main__':
    print V1_99(1,9）
