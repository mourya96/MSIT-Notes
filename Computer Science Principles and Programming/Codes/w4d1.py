# a, b = input().strip().split(" ")
# a = a == "True"
# b = b == 'True'

# print(a and b)
# print(a or b)
# print(not a, not b)

# Monkey Trouble
# a = input() == 'True'
# b = input() == 'True'

# def monkey_trouble(a, b):
#     return (a and b) or (not a and not b)

# print(monkey_trouble(a, b))

# Posneg
# a = int(input())
# b = int(input())
# c = input() == 'True'

# def posneg(a, b, c):
#     return (((not c) and a*b < 0) or (c and a < 0 and b < 0))

# print(posneg(a, b, c))

# Longest Increasing Run
# def checkIncreasing(n):
#     count = 1
#     if n < 10:
#         return n
#     previous = n % 10
#     n //= 10
#     current = n % 10
#     while(n > 0):
#         if previous > current:
#             count += 1
#         else:
#             return count
#         previous = current
#         n //= 10
#         current = n % 10
#     return count

# def increasingRun(n):
#     max_run = float("-inf")
#     max_output = float("-inf")
#     while(n > 0):
#         c = checkIncreasing(n)
#         if c >= max_run:
#             max_run = c
#             m = n % (10**c)
#             if m > max_output:
#                 max_output = m
#         n //= (10**c)
#     return max_output

# print(increasingRun(abs(int(input()))))

# mostFrequentDigit


# def mostFrequentDigit(n):
#     max_count = float("-inf") 
#     min_num = float("inf")
#     for i in range(10):
#         count = 0
#         temp = n
#         while(temp > 0):
#             if temp%10 == i:
#                 count += 1
#             temp //= 10
        
#         if count == max_count and min_num > i:
#             min_num = i
#         elif count > max_count:
#             max_count = count
#             min_num = i
    
#     return min_num

# print(mostFrequentDigit(int(input())))

# gcd

# def gcd(a, b):
#     while (b > 0):
#         a, b = b, a % b
#     return a

# print(gcd(int(input()), int(input())))

# nthAnthromorphic number

# def count_digits(n):
#     count = 0
#     while(n > 0):
#         count += 1
#         n //= 10
#     return count

# def is_anthromorphic(n):
#     count = count_digits(n)
#     return n == (n**2) % (10**count)

# def nth_anthromorphic(n):
#     c = 1
#     num = 0
#     while(c <= n):
#         if is_anthromorphic(num):
#             c += 1
#         num += 1
#     return num - 1

# n = int(input())

# print(nth_anthromorphic(n))

# nthLeftTruncatablePrime

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def is_left_truncatable_prime(n):
#     m = 0
#     c = 0
#     while (n > 0):
#         m = 10**c * (n % 10) + m
#         c += 1
#         n //= 10
#         if not is_prime(m):
#             return False
    
#     return True


# def nth_left_truncatable_prime(n):
#     c = 1
#     num = 2
#     while(c <= n):
#         if is_left_truncatable_prime(n):
#             c += 1
#         num += 1
#     return num -1

# print(nth_left_truncatable_prime(int(input())))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_powerful(n):
    if n != 1 and n < 4:
        return False
    for i in range(2, int(n**0.5)+1):
        if is_prime(i):
            if n % i == 0:
                if n % (i**2) != 0:
                    return False
            else:
                continue
        else:
            continue
            
    return True

def nth_powerful(n):
    c = 0
    num = 1
    while (c <= n):
        if is_powerful(num):
            c += 1
        num += 1
    return num - 1

print(nth_powerful(int(input())))