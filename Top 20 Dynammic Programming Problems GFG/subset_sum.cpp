#include <stdio.h> 
#include<bits/stdc++.h>
using namespace std;
bool isSubsetSum(int set[], int n, int sum) 
{ 

	bool subset[n + 1][sum + 1]; 
	for (int i = 0; i <= n; i++) 
		subset[i][0] = true; 

	for (int i = 1; i <= sum; i++) 
		subset[0][i] = false; 

	for (int i = 1; i <= n; i++) { 
		for (int j = 1; j <= sum; j++) { 
			if (j < set[i - 1]) 
				subset[i][j] = subset[i - 1][j]; 
			if (j >= set[i - 1]) 
				subset[i][j] = subset[i - 1][j] 
							|| subset[i - 1][j - set[i - 1]]; 
		} 
	} 
	return subset[n][sum]; 
} 

int main() 
{ 
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int ar[100];
	int input;
	int k=0;
	int sum;
	while (cin >> input)
	{
		ar[k++] = input;
	}
	cin >> sum;
	if (isSubsetSum(ar, k+1, sum) == true)
		cout << "True";
	else
		cout << "False";
	
	
	return 0; 
} 