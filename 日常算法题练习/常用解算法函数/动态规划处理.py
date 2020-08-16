# 【1，11，2，6，5】从中取最大值,且只能间隔取
# 动态规划思路： 将最后一个处理思想为： 选  与  不选
# 当Opt(arr[n])选着时 ，此时他与Opt(arr[n-2])+arr[n]有关系，当不选时，他与Opt(arr[n-1])有关系

# 递归
def rec_opt(arr: list):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr[:len(arr) - 2]) + arr[len(arr) - 1]
        B = rec_opt(arr[:len(arr) - 1])
        return max(A, B)


print(rec_opt([1, 11, 2, 6, 5]))


# 非递归
def dp_opt(arr: list):
    dp = [0 for _ in range(len(arr))]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = dp[i - 2] + arr[i]
        B = dp[i - 1]
        dp[i] = max(A, B)
    return dp[len(arr) - 1]


print(dp_opt([1, 11, 2, 6, 5]))


# 【1，11，2，6，5】从中取是否有那满足等于S=9的值
# 递归
def rec_subset(arr, i, S):
    if S == 0:
        return True
    elif i == 0:
        return arr[0] == S
    elif arr[i] > S:
        return rec_subset(arr, i - 1, S)
    else:
        A = rec_subset(arr, i - 1, S - arr[i])
        B = rec_subset(arr, i - 1, S)
        return A or B


print(rec_subset([1, 11, 2, 6, 5], 4, 9))
print(rec_subset([1, 11, 2, 6, 5], 4, 4))


# 非递归
def dp_subset(arr, S):
    dp = [[0 for _ in range(S + 1)] for _ in range(len(arr))]
    for i in dp:
        i[0] = True
    for i in range(len(dp[0])):
        dp[0][i] = False
    dp[0][arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S + 1):
            if arr[i] > S:
                dp[i][s] = dp[i - 1][s]
            else:
                A = dp[i - 1][s - arr[i]]
                B = dp[i - 1][s]
                dp[i][s] = A or B
    r, c = len(dp), len(dp[0])
    return dp[r - 1][c - 1]


print(dp_subset([3, 34, 4, 12, 5, 2], 9))
