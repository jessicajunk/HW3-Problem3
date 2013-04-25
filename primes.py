#Returns a list of all prime numbers up through n numbers
%cython
def find_primes2(long n):
    numlist = []
    primelist = []
    for i in range(2, n + 1):
        numlist.append(i)
    while len(numlist) != 0:
        primelist.append(numlist[0])
        p = numlist[0]
        for i in numlist:
            if i % p == 0:
                numlist.remove(i)
    return primelist
