__author__ = 'qiong'
# for epi 12.14

def compute_binomial_coefficent(n, k):
    table = [[0 for j in k+1] for i in n+1]


    for i in range(n+1):
        table[i][0] = 1

    for j in range(1, k+1):
        table[1][j] = 1

    for i in range(2, n+1):
        for j in range(1, k+1):
            if j<i:
                table[i][j] = table[i-1][j]+table[i-1][j-1]
            else:
                break

    return table[n][k]