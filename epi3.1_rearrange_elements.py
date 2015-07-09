__author__ = 'qiong'

# time complexity O(n)
# space complexity O(1)

def dutch_flag_partition(s, p_idx):
    pivot = s[p_idx]
    small = 0; equal = 0
    large = len(s)-1
    while equal<=large:
        if s[equal]==pivot:
            equal += 1
        elif s[equal]<pivot:

            s[equal], s[small] = s[small], s[equal]

            equal+=1
            small += 1
        else:

            s[equal], s[large] = s[large], s[equal]
            large -= 1

s = [6, 4, 9, 2]
dutch_flag_partition(s, 1)
print s