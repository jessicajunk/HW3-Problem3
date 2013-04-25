HW3-Problem3
============

Computes a list of prime numbers up through n numbers, up to 10000.

Example: find_primes(100) --> 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

code in python: timeit("find_primes(10000)") --> 5 loops, best of 3: 554 ms per loop

code in cython: timeit("find_primes(10000)") --> 5 loops, best of 3: 481 ms per loop
