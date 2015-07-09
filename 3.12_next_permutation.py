__author__ = 'qiong'
# time complexity O(n)
# space complexity O(n)

def next_permutation(num):
    if not num: return None
    k = len(num)-2
    while k>=0 and num[k]>=num[k+1]:
        k-=1
    if k==-1: return None

    for i in range(len(num)-1, k, -1):
        if num[i]>num[k]:
            num[i], num[k] = num[k], num[i]

    res = num[:k+1]+num[:k:-1]
    return res

print next_permutation([1, 4, 5, 3, 2])