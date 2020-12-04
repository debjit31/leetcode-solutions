
/// Minimum Sum partition :- 
/*
 Case 1 :- Find the minimum difference :- res = sum - 2*i;
 Case 2:-  Find  the maximum sum between the 2 subsets after minimum partition :- res = sum - i;
*/

#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int findMin(vector<int> &ar, int n){
	int sum = 0;
	for(int i=0;i<n;i++)
		sum += ar[i];
	
	bool dp[n+1][sum+1];
	for(int i=0;i<=n;i++)
		dp[i][0] = true;
		
	for(int j=1; j<=sum; j++)
		dp[0][j] = false;
		
	for(int i=1; i<=n;i++){
		for(int j=1;j<=sum;j++){
			dp[i][j] = dp[i-1][j];
			if(ar[i-1] <= j)
				dp[i][j] |= dp[i-1][j -ar[i-1]];
		}
	}
	int res = INT_MAX;
	for(int i=sum/2 ; i>=0; i--)
	{
		if(dp[n][i] == true){
			// for the difference between 2 sets after minimum partition
			//res = sum - 2*i;
			// for the set having larger sum after minimum partition , set with samller sum
			// can be obtained by abs(sum - res)
			res = sum - i;
			break;
		}
	}
	return res;
	
}
int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	vector<int> ar;
	int input;
	while(cin>>input){
		ar.push_back(input);
	}
	int sum = 0;
	for(int i=0;i<ar.size();i++)
		sum += ar[i];
	int ms = findMin(ar, ar.size());
	//cout << abs(sum-ms) << "\n";
	cout << ms << "";
	return 0;
}