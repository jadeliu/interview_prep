__author__ = 'qiong'
# time complexity: varies; average O(log n)? worst O(n)
# space complexity: O(1)

def find_longest_increasing_subarray(s):
    max_len = 1
    idx = 0
    while idx<len(s):
        is_skippable = False
        for j in range(idx+max_len-1, idx, -1):
            if s[j]>=s[j+1]:
                is_skippable = True
                idx = j+1
                break
        # look forward
        if is_skippable==False:
            idx += max_len-1
            while idx<len(s) and s[idx]<s[idx+1]:
                idx += 1
                max_len += 1
    return (idx-max_len+1, idx)


s = [3, 1, 2, 4, 6, 0, 5]
print find_longest_increasing_subarray(s)