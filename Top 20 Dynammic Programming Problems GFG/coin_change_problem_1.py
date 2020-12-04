def minNoofCoins(amount, coins):
	dp = [amount+1 for i in range(amount+1)]
	coins.sort()
	dp[0] = 0
	for i in range(amount+1):
		for c in coins:
			if c<=i:
				dp[i] = min(dp[i], 1+dp[i - c])
			else:
				break
	return -1 if dp[amount] > amount else dp[amount]



coins = list(map(int, input().split()))
amount = int(input())
print(minNoofCoins(amount, coins))