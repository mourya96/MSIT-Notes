# def factorial(n):
#     output = 1
#     for i in range(1,n+1):
#         output *= i
#     return output

# n = int(input())
# print(factorial(n))

# def calculate_power(a, b):
#     output = 1
#     for i in range(b):
#         output *= a
#     return output

# a, b = map(int, input().strip().split(" "))

# print(calculate_power(a, b))

# def prime_check(n):
#     if n == 1 or n == 0:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# print(prime_check(int(input())))

# def three_or_five(n):
#     output = 0
#     for i in range(1, n):
#         if i % 5 == 0 or i % 3 == 0:
#             output += i
#     return output

# print(three_or_five(int(input())))

# def gen_table(n, m):
#     for i in range(1, m+1):
#         print(f'{n} * {i} = {n*i}')
# n, m = map(int, input().strip().split(" "))

# gen_table(n, m)

import math
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_carol(n):
    m = int(math.log((n+2)**0.5 + 1, 2))
    if (2**m - 1)**2 - 2 == n:
        return True
    else:
        return False

def carol_prime(n):
    if  is_carol(n) and is_prime(n):
        return True
    else:
        return False

# print(carol_prime(int(input())))

# def isHappyNumber(n):
#     while(n >= 10):
#         s = 0
#         while(n != 0):
#             s += (n % 10)**2
#             n = n // 10
#         n = s
#     if n == 1:
#         return True
#     else:
#         return False

# print(isHappyNumber(abs(int(input()))))

# def isPalindrome(n):
#     n = str(n)
#     if n == n[::-1]:
#         return True
#     else:
#         return False

# def isPrime(n):
#     if n == 1 or n == 0:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def isPalindromePrime(n):
#     if isPrime(n) and isPalindrome(n):
#         return True
#     else:
#         return False
    
# print(isPalindromePrime(int(input())))

def carrylessAdd(a, b):
    output = ''
    if a == 0 and b == 0:
        return 0
    while(a != 0 or b != 0):
        s = ((a % 10) + (b % 10))
        a, b = a // 10, b // 10
        if s == 0 and (a == 0 or b == 0):
            break
        else:
            output = str(s%10) + output
    return int(output)

print(carrylessAdd(int(input()), int(input())))