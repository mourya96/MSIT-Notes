# def sumDigits(n):
#     s = 0
#     while(n > 0):
#         s += (n % 10)
#         n = n // 10
#     return s

# def isTenly(n):
#     return sumDigits(n) == 10

# def isPrime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# def isTenlyPrime(n):
#     return isTenly(n) and isPrime(n)

# def nthTenlyPrime(n):
#     c = 0
#     num = 19
#     while(c <= n):
#         if isTenlyPrime(num):
#             c += 1
#         num += 1
#     return num-1

    
# n = int(input())

# print(nthTenlyPrime(n))


# def isTidy(n):
#     current_digit = n % 10
#     while(n > 0):
#         if current_digit < (n % 10):
#             return False
#         current_digit = (n % 10)
#         n = n // 10
#     return True

# def nthTidyNumber(n):
#     c = 0
#     num = 1
#     while(c <= n):
#         if isTidy(num):
#             c += 1
#         num += 1
#     return num - 1

# print(nthTidyNumber(int(input())))


# def isPrime(n):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True

# def isPalindrome(n):
#     m = 0
#     temp = n
#     while(temp > 0):
#         m = m*10 + (temp % 10)
#         temp //= 10
#     return m == n

# def isPalindromePrime(n):
#     return isPalindrome(n) and isPrime(n)

# def nthPalindromePrime(n):
#     c = 0
#     num = 2
#     while(c <= n):
#         if isPalindromePrime(num):
#             c += 1
#         num += 1
#     return num - 1

# print(nthPalindromePrime(int(input())))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def sum_digits(n):
#     s = 0
#     while (n > 0):
#         s += (n % 10)
#         n //= 10
#     return s

# def is_additive_prime(n):
#     return is_prime(sum_digits(n)) and is_prime(n)

# def nth_additive_prime(n):
#     c = 0
#     num = 2
#     while(c <= n):
#         if is_additive_prime(num):
#             c += 1
#         num += 1
#     return num-1

# n = int(input())

# print(nth_additive_prime(n))

# import math
# def is_prime(n):
#     if n == 1 or n == 0:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def is_carol(n):
#     m = int(math.log((n+2)**0.5 + 1, 2))
#     if (2**m - 1)**2 - 2 == n:
#         return True
#     else:
#         return False

# def carol_prime(n):
#     if  is_carol(n) and is_prime(n):
#         return True
#     else:
#         return False

# def nth_carol_prime(n):
#     c = 0
#     num = 7
#     while(c <= n):
#         if carol_prime(num):
#             c += 1
#         num += 1
#     return num - 1

# n = int(input())

# print(nth_carol_prime(n))

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def rotate_number(n):
    if n < 10:
        return n
    last_digit = n % 10
    return int(str(last_digit) + str(n // 10))

def is_circular_prime(n):
    m = rotate_number(n)
    while(m != n):
        if not is_prime(m):
            return False
        m = rotate_number(m)
    return is_prime(n)

def nth_circular_prime(n):
    c = 0
    num = 2
    while (c <= n):
        if is_circular_prime(num):
            c += 1
        num += 1
    return num - 1
n = int(input())

print(nth_circular_prime(n))