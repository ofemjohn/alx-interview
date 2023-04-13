#!/usr/bin/python3
import sys
'''
Write a script that reads stdin line
 by line and computes metrics:
'''


def print_stats(total_file_size, code_counts):
    print("File size:", total_file_size)
    for code, count in code_counts.items():
        if count > 0:
            print(f"{code}: {count}")


total_file_size = 0
code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
for i, line in enumerate(sys.stdin, start=1):
    fields = line.strip().split()
    file_size = int(fields[-1])
    status_code = fields[-2]
    total_file_size += file_size
    code_counts[status_code] += 1
    if i % 10 == 0:
        print_stats(total_file_size, code_counts)
print_stats(total_file_size, code_counts)
