__author__ = 'qiong'

'''
Given two strings S and T, determine if they are both one edit distance apart.


'''
# time complexity: O(n)
# space complexity: O(1)
# time spent: 35mins
def one_edit(str1, str2):

    m = len(str1)
    n = len(str2)
    if abs(m-n)>1:
        return False
    if m>n: return one_edit(str2, str1)
    dif = n-m
    idx = 0
    while idx<m and str1[idx]==str2[idx]:
        idx += 1
    if idx==m==n: return False
    # pointer reach first char that's different
    if dif==0:
        idx += 1
    while idx<m and str1[idx]==str2[idx+dif]:
        idx+=1
    return idx==m

print one_edit('abbb', 'abb')
print one_edit('', 'a')
print one_edit('abcc', 'abb')
print one_edit('','')
print one_edit('LinkedIn is the worlds largest business network, helping professionals like Jauhar Basrai discover inside','LinkedIn is the worlds  largest business network, helping professionals like Jauhar Basrai discover inside')