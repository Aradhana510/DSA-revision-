Q1. Find All Primes
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
Given an integer A. Find the list of all prime numbers in the range [1, A].


Problem Constraints
1 <= A <= 106



Input Format
Only argument A is an integer.



Output Format
Return a sorted array of prime number in the range [1, A].



Example Input
Input 1:
A = 7
Input 2:
A = 12


Example Output
Output 1:
[2, 3, 5, 7]
Output 2:
[2, 3, 5, 7, 11]


Example Explanation
For Input 1:
The prime numbers from 1 to 7 are 2, 3, 5 and 7.
For Input 2:
The prime numbers from 1 to 12 are 2, 3, 5, 7 and 11.



SOLUTION



import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        primes = [True] * (A+1)
        pos = int(math.sqrt(A))

        for i in range(2,pos+1):
            if primes[i]:
                for j in range(i*i,A+1,i):
                    if primes[j]:
                        primes[j] = False
        res = []
        for i in range(2,A+1):
            if primes[i]:
                res.append(i)
        return res