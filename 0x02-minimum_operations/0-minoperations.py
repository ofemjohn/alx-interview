#!/usr/bin/python3
'''
using the minimum operation to copy and past
a character H until it amounts to the function
arguments value
'''


def minOperations(n):
    if n < 1:
        return 0
    
    clipboard_copy = 1
    current_h = 1
    num_ops_count = 0
    
    while current_h < n:
        if n % current_h == 0:
            clipboard_copy = current_h
            num_ops_count += 1
        
        current_h += clipboard_copy
        num_ops_count += 1
        
    return num_ops_count
