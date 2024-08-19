Q4. Prime Sum
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.

If there is more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.



Problem Constraints
4 <= A <= 2*107



Input Format
First and only argument of input is an even number A.



Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.



Example Input
 4


Example Output
 [2, 2]


Example Explanation
 There is only 1 solution for A = 4.

SOLUTION

import math
class Solution:

	# @param A : integer
	# @return a list of integers
    def primenumb(self, N):
        primes = [True]*(N+1)
        pos =  int(math.sqrt(N))
        for i in range(2,pos+1):
            if primes[i] :
                for j in range(i*i,N+1,i):
                    if primes[j] == True:
                        primes[j] = False
        res = [i for i in range(2,N+1) if primes[i] ]
        return res

	def primesum(self, A):
        array = self.primenumb(A)
        l,r = 0, len(array) - 1
        while l <= r:
            if array[l] + array[r] == A:
                return [array[l],array[r]]
            elif array[l] + array[r] > A:
                r -= 1
            else:
                l += 1
        