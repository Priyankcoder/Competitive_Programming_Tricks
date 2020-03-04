'''
Sieve of Eratosthenes in 0(n) time complexity
The classical Sieve of Eratosthenes algorithm takes O(N log (log N)) time to find all prime numbers less than N. In this article, a modified Sieve is discussed that works in O(N) time.

Example :

Given a number N, print all prime 
numbers smaller than N

Input :  int N = 15
Output : 2 3 5 7 11 13

Input : int N = 20
Output : 2 3 5 7 11 13 17 19


Approach:


Manipulated Sieve of Eratosthenes algorithm works as following:



For every number i where i varies from 2 to N-1:
    Check if the number is prime. If the number
    is prime, store it in prime array.

For every prime numbers j less than or equal to the smallest  
prime factor p of i:
    Mark all numbers j*p as non_prime.
    Mark smallest prime factor of j*p as j

'''    


#Implementation


# Python3 program to generate all  
# prime numbers less than N in O(N)  
  
MAX_SIZE = 1000001
  
# isPrime[] : isPrime[i] is true if 
#             number is prime  
# prime[] : stores all prime number  
#           less than N  
# SPF[] that store smallest prime  
# factor of number [for ex : smallest  
# prime factor of '8' and '16'  
# is '2' so we put SPF[8] = 2 ,  
# SPF[16] = 2 ]  
isprime = [True] * MAX_SIZE  
prime = []  
SPF = [None] * (MAX_SIZE)  
  
# function generate all prime number  
# less then N in O(n)  
def manipulated_seive(N):  
  
    # 0 and 1 are not prime  
    isprime[0] = isprime[1] = False
  
    # Fill rest of the entries  
    for i in range(2, N):  
      
        # If isPrime[i] == True then i is  
        # prime number  
        if isprime[i] == True:  
          
            # put i into prime[] vector  
            prime.append(i)  
  
            # A prime number is its own smallest  
            # prime factor  
            SPF[i] = i  
          
        # Remove all multiples of i*prime[j]  
        # which are not prime by making is 
        # Prime[i * prime[j]] = false and put 
        # smallest prime factor of i*Prime[j] 
        # as prime[j] [ for exp :let i = 5 , j = 0 , 
        # prime[j] = 2 [ i*prime[j] = 10 ]  
        # so smallest prime factor of '10' is '2'  
        # that is prime[j] ] this loop run only one  
        # time for number which are not prime  
        j = 0
        while (j < len(prime) and
               i * prime[j] < N and
                   prime[j] <= SPF[i]): 
          
            isprime[i * prime[j]] = False
  
            # put smallest prime factor of i*prime[j]  
            SPF[i * prime[j]] = prime[j] 
              
            j += 1
          
# Driver Code 
if __name__ == "__main__":  
  
    N = 13 # Must be less than MAX_SIZE  
  
    manipulated_seive(N)  
  
    # print all prime number less then N  
    i = 0
    while i < len(prime) and prime[i] <= N: 
        print(prime[i], end = " ")  
        i += 1
          

# Source - geeksForgeeks