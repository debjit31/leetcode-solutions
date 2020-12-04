# Given two strings str1 and str2 and below operations that can performed on str1. 
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  

# Insert
# Remove
# Replace
# All of the above operations are of equal cost. 



def editDistance(s,t):
	m = len(s)
	n = len(t)
	dp = [[0 for j in range(n+1)] for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif s[i-1] == t[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
	return dp[m][n]
	
	
s = input()
t = input()
print(editDistance(s,t))




