'''
Problem:
	Climbing Stairs (k steps)

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps.
	In how many distinct ways can you climb to the top?

'''

# Time complexity: O(nk)
# Space complexity: O(n)
def climbStairsKSteps(n: int, k: int) -> int:
	dp: list = [0] * (n+1)
	dp[0] = 1
	for i in range(1, n+1):
		for j in range(1, k) :
			if i-j < 0 :
				continue
			dp[i % k] += dp[(i-j) % k]
	return dp[n % k]

print(climbStairsKSteps(3, 2))
print(climbStairsKSteps(5,2))
print(climbStairsKSteps(3, 3))
print(climbStairsKSteps(1000, 2))
