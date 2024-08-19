Q3. Sorted Permutation Rank
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003



Problem Constraints
1 <= |A| <= 1000



Input Format
First argument is a string A.



Output Format
Return an integer denoting the rank of the given string.



Example Input
Input 1:

A = "acb"
Input 2:

A = "a"


Example Output
Output 1:

2
Output 2:

1


Example Explanation
Explanation 1:

Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.
Explanation 2:

Given A = "a".
Rank is clearly 1.

SOLUTION

class Solution:
	# @param A : string
	# @return an integer
    mod = 1000003
    def nfact(self,n):
        if(n==0 or  n==1):
            return 1
        else:
            return (n*self.nfact(n-1)) % self.mod
	def findRank(self, A):
        n = len(A)
        ans = 0
        for i in range(n-1):
            count = 0
            for j in range(i+1,n):
                if A[i] > A[j]:
                    count += 1
            pos = n - i - 1
            ans += (count * self.nfact(pos)) % self.mod
        return (ans + 1) % self.mod