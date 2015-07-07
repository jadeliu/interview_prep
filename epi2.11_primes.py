__author__ = 'qiong'
import math

# start time 8:52pm
# finish time 9:34pm
# time complexity O(log n)?

def generate_primes(n):
    if n==1:
        return []
    if n==2:
        return [2]
    size = int(math.floor(0.5*(n-3))+1) # starts from 3

    primes = [2]
    is_prime = [True for i in range(size)]
    for i in xrange(size):
        if is_prime[i]:
            p = (i<<1)+3
            primes.append(p)
            j = int(((i*i)<<1)+6*i+3) # p^2
            for j in range(j, size, p):
                is_prime[j] = False

    return primes

print generate_primes(14)