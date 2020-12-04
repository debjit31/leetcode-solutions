def minNoofCoins(amount, coins):
	count = [0 for i in range(amount+1)]
	count[0] = 1
	for c in coins:
		for j in range(c, amount+1):
			count[j]+= count[j-c]
	return count[amount]




coins = list(map(int, input().split()))
amount = int(input())
print(minNoofCoins(amount, coins))
