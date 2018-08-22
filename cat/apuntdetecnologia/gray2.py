#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 d’ag. 2018
@author: albert
https://ca.wikipedia.org/wiki/Codi_Gray
'''

def calculate_gray(number, n):
    bits = []
    gray = []
    
    remainder = number
    for nn in range(0, n):
        [quotient, remainder] = divmod(remainder, 2 ** (n - 1 - nn))
        bits.append(quotient)
        if nn == 0:
            gray.append(bits[0])
        else:
            gray.append(bits[nn - 1] ^ bits[nn])      
            
            
    return [bits, gray]

def calculate_binary(gray, n):  # gray is an array of bits
    bits = []

    for pos in range(0, n):
        if pos == 0:
            bits.append(gray[0])
        else:
            bits.append(bits[pos - 1] ^ gray[pos])      
            
    return bits


if __name__ == '__main__':
    print "print a Gray table for n bits"
    n = raw_input('Number of bits? ')
    n = int(n)
    print "number of bits : %d" % n   
    
    bits = []
    gray = []
    grayTable = []

    for i in range(0, 2 ** n):
        [bits, gray] = calculate_gray(i, n)
        grayTable.append(gray)
        strBits = ''.join(map(lambda (x) : chr(ord('0') + x), bits))
        strGray = ''.join(map(lambda (x) : chr(ord('0') + x), gray))
        
        print "%5d --> %s --> %s" % (i, strBits, strGray)
    
    print "-------------------------------------------"
    
    bits = []

    for i in range(0, 2 ** n):
        bits = calculate_binary(grayTable[i], n)
        strBits = ''.join(map(lambda (x) : chr(ord('0') + x), bits))
        strGray = ''.join(map(lambda (x) : chr(ord('0') + x), grayTable[i]))
        
        print "%5d --> %s --> %s" % (i, strGray, strBits)

    print "Done!"