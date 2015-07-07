__author__ = 'qiong'


def test_bit(n):
    return n & (n>>1<<1)

def is_odd(n):
    return not test_bit(n)

def is_even(n):
    return test_bit(n)

def gcd(a, b):
    if a==0:
        return b
    elif b==0:
        return a
    elif is_even(a) and is_even(b):
        return gcd(a>>1, b>>1)<<1
    elif is_odd(a) and is_even(b):
        return gcd(a, b>>1)
    elif is_even(a) and is_odd(b):
        return gcd(a>>1, b)
    elif a<=b:
        return gcd(a, b-a)
    else:
        return gcd(a-b, b)

print gcd(6, 12)
