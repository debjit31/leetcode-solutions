# Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

# Input: n = 3
# Output: 4
# Explantion:
# Below are the four ways
#  1 step + 1 step + 1 step
#  1 step + 2 step
#  2 step + 1 step
#  3 step



def noofWays(n):
	dp=[0 for i in range(n+1)]
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	for i in range(4, n+1):
		dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
	return dp[n]



for _ in range(int(input())):
	n = int(input())
	print(noofWays(n))