import math

__author__ = 'qiong'

# start time 4:56pm
# finish time 5:23pm
# time complexity 2^n

def generate_power_set(s):
    if not s: return []
    res = []
    for i in xrange(1<<len(s)):
        x = i
        subset = []
        while x:
            tar = int(math.log((x and (not (x-1))), 2))
            subset.append(s[tar])
            x = x and (x-1)
        res.append(','.join(subset))
    return res

s = ['l', 'g', 'e']
print generate_power_set(s)