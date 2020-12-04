# Cutting a Rod

# Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

def rodCutting(pieces, n):
	cut = [0 for _ in range(n+1)]
	cut[0] = 0
	for i in range(1, n+1):
		mv = -9999999
		for j in range(i):
			mv = max(mv, pieces[j] + cut[i-j-1])
		cut[i] = mv
	return cut[n]



pieces = list(map(int, input().split(', ')))
print(rodCutting(pieces, len(pieces)))