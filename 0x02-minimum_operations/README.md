# Minimum Operations

## QUESTIONS
```In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```






```Here's an approach you can follow:

Initialize a counter variable "count" to 0 and a variable "clipboard" to 0.
While the current number of "H"s is less than n:
a. If n is divisible by the current number of "H"s, set clipboard to the current number of "H"s and copy all.
b. Otherwise, paste the content of the clipboard to the end of the file.
c. Increment the count by 1.
d. Update the current number of "H"s to the new length of the file.
If the current number of "H"s is equal to n, return the count. Otherwise, return 0.
```