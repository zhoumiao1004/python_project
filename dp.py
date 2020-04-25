# coding:utf-8


# 1.爬楼梯,一次能走一步或两步
# n = 10
# A: 89
def get_all_path_count(n):
    if n <= 2:
        return n
    l = [1, 2]
    for i in range(3, n):
        l[0], l[1] = l[1], l[0] + l[1]
    return l[0] + l[1]


# 2.最长上升子序列 LIS
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
# A: 4
def get_lis_length(arr):
    opt = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                opt[i] = max(opt[i], opt[j] + 1)
    return opt[-1]


# 3.连续子数组最大和
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# A: 6
def get_max_count(arr):
    m = arr[0]
    sum = arr[0]
    for num in arr[1:]:
        sum = sum + num if sum > 0 else num
        m = max(m, sum)
    return m


# 4.求两字符串的连续最大公共子字符串(The Longest Common Substring) LCS（序列可以不连续）
# programming contest
# 2 (on)
def get_lcs_length(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    m = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]  # n2行n1列
    for i in range(1, n2 + 1):
        for j in range(1, n1 + 1):
            if str1[j - 1] == str2[i - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])
    return m[-1][-1]


# 5.背包问题knapsack
def knapsack(w, v, C):
    import numpy as np
    mem = np.zeros((len(w) + 1, C + 1))
    for i in range(1, len(w) + 1):
        value = v[i - 1]
        weight = w[i - 1]
        for j in range(1, C + 1):
            if weight > j:
                mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = max(mem[i - 1][j], mem[i - 1][j - w[i - 1]] + value)
    return mem


# 6.找钱
def coin_change(coins, amount):
    if len(coins) == 0:
        return -1
    if amount == 0:
        return 0
    if len(coins) == 1 and coins[0] > amount:
        return -1
    m = [-1] * (amount + 1)
    m[0] = 0
    for i in range(1, amount + 1):
        cur_min = amount + 1
        for c in coins:
            if c <= i:
                cur_min = m[i - c] if m[i - c] < cur_min else cur_min
        m[i] = cur_min + 1 if cur_min < amount + 1 else amount + 1
    if m[-1] == amount + 1:
        return -1
    else:
        return m[-1]


if __name__ == '__main__':
    print get_all_path_count(10)
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print get_lis_length(arr)
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print get_max_count(arr)
    print get_lcs_length('programming', 'contest')
    print coin_change([1, 2, 5], 11)
    print coin_change([1, 2, 5], 13)
