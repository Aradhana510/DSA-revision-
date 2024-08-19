Q1. Lucky Numbers
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints except Complete Solution is Penalty free now
Use Hint
Problem Description
A lucky number is a number that has exactly 2 distinct prime divisors.

You are given a number A, and you need to determine the count of lucky numbers between the range 1 to A (both inclusive).



Problem Constraints
1 <= A <= 50000



Input Format
The first and only argument is an integer A.



Output Format
Return an integer i.e the count of lucky numbers between 1 and A, both inclusive.



Example Input
Input 1:

 A = 8
Input 2:

 A = 12


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 Between [1, 8] there is only 1 lucky number i.e 6.
 6 has 2 distinct prime factors i.e 2 and 3.
Explanation 2:

 Between [1, 12] there are 3 lucky number: 6, 10 and 12.


SOLUTION

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Sieve of Eratosthenes to generate prime numbers up to A
        is_prime = [True] * (A + 1)
        is_prime[0] = is_prime[1] = False
        primes = []
        for i in range(2, int(A**0.5) + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, A + 1, i):
                    is_prime[j] = False
        
        # Count distinct prime factors for each number in the range [1, A]
        lucky_count = 0
        for num in range(1, A + 1):
            distinct_factors = 0
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    distinct_factors += 1
                    while num % prime == 0:
                        num //= prime
            if num > 1:
                distinct_factors += 1
            if distinct_factors == 2:
                lucky_count += 1
        
        return lucky_count