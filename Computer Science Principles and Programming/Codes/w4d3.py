# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# n = int(input())

# print(factorial(n))

# def count_digits(n):
#     n = abs(n)
#     if n == 0:
#         return 1
#     count = 0
#     while(n != 0):
#         count += 1
#         n //= 10
#     return count

# n = int(input())
# print(count_digits(n))

# def sum_digits(n):
#     n = abs(n)
#     s = 0
#     while(n != 0):
#         s += (n % 10)
#         n //= 10
#     return s

# n = int(input())
# print(sum_digits(n))

# def conjecture(n):
#     steps = 0
#     while(n != 1):
#         steps += 1
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = n*3 + 1
#     return steps

# n = int(input())
# print(conjecture(n))

# def sum_digits(n):
#     s = 0
#     while(n != 0):
#         s += (n % 10)
#         n //= 10
#     return s

# n = abs(int(input()))

# while len(str(n)) > 1:
#     n = sum_digits(n)

# print(n)

def longest_digit(n):
    elem = float('inf')
    maxi = 0
    count = 0
    while n//10 != 0:
        prev = n%10
        n = n//10
        present = n%10
        if prev == present:
            count += 1
        else:
            if count >= maxi:
                if count == maxi and elem > prev:
                    elem = prev
                    maxi = count
                    count = 0
    return elem

n = abs(int(input()))
print(longest_digit(n))