def maxEnergy(mat):
    n = len(mat)
    m = len(mat[0])
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = mat[i][j]
            elif i == 0:
                dp[i][j] = mat[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = mat[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = mat[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    return dp[n - 1][m - 1]


if __name__ == '__main__':
    mat = [[10, 20, 30, 40], [60, 50, 20, 80], [10, 10, 10, 10], [60, 50, 60, 50]]
    print(maxEnergy(mat))