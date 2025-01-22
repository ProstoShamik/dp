'''
    Problem:
    Find sum of the first N elements.

    Objective function:
    f(i) is the sum of the first i elements.

    Recurrence relation:
    f(n) = f(n - 1) + n

'''

# n = 0 
def nSum(n: int) -> int:
    if n < 0:
        return None
    dp: list = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp[n]

print(nSum(0))
print(nSum(1))
print(nSum(5))
print(nSum(15))
print(nSum(20))
