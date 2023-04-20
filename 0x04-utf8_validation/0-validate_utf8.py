#!/usr/bin/env python3
'''working with utf-8'''


def validUTF8(data):
    '''a utf-a f'''
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
