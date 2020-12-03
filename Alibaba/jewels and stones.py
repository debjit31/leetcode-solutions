def countJewelsandStones(J,S):
	jewels = {}
	for i in J:
		jewels[i] = 1
	c=0
	for i in range(len(S)):
		try:
			if jewels[S[i]] == 1:
				c+=1
		except Exception as e:
			pass
	return c
	
J = input()
S = input()
print(countJewelsandStones(J,S))