#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
'''
Created on 19 d’ag. 2018

@author: albert
'''

def calculate_gray(i, n):
    bits = []
    
    for nn in range(0, n):
        if nn == 0:
            middle = 2 ** (n - 1) 
            if (i < middle):
                bits.append('0')
            else:
                bits.append('1')
    
        if nn > 0 and nn < (n - 1) and n>2:
            if nn == 1:            
                min1 = 0
                max1 = 2 ** (n - 2)
                min2 = 2 ** n  -  2 ** (n - 2)
                max2 = 2 ** n 
                rang = (range(min1, max1) + range(min2, max2))
            else:
                min1 = 0
                max1 = 2 ** (n - nn - 1)
                min2 = 2 ** (n - nn + 1) - 2 ** (n - nn - 1)
                max2 = 2 ** (n - nn + 1)
                rang = (range(min1, max1) + range(min2, max2))
            
            
            if (i % (2 ** (n - nn + 1))) in rang:
                bits.append('0')
            else:
                bits.append('1')            

        if nn == n - 1:
            if (i % 4) in (0, 3):
                bits.append('0')
            else:
                bits.append('1')
        
    return bits

if __name__ == '__main__':
    print "print a Gray table for n bits"
    n = raw_input('Number of bits? ')
    n = int(n)
    print "number of bits : %d" % n   
    bits = ''

    for i in range(0, 2 ** n):
        bits = calculate_gray(i, n)
                
        print '%5d --> %s' % (i, ''.join(bits))  
        
    print "Done!"
    
