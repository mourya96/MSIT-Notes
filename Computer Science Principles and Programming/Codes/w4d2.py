# def is_multiple(n1, n2):
#     if n1 == 0:
#         return True
#     elif n2 == 0:
#         return False
    
#     if n1 % n2 == 0:
#         return True
#     else:
#         return False
    
# n1 = int(input())
# n2 = int(input())

# print(is_multiple(n1, n2))

# def fabricYards(n):
#     if n % 36 == 0:
#         return n // 36
#     else:
#         return (n // 36) + 1

# n = int(input())
# print(fabricYards(n))

# def eggs(n):
#     if n % 12 == 0:
#         return n // 12
#     else:
#         return n // 12 + 1
# n = int(input())

# print(eggs(n))

# def isLegalTriangle(a, b, c):
#     if a + b > c and b + c > a and c + a > b:
#         return True
#     else:
#         return False
    
# a = float(input())
# b = float(input())
# c = float(input())

# print(isLegalTriangle(a, b, c))

# def gym(age, bmi, health_condition):
#     if (not health_condition) and (bmi > 18.5 and bmi < 24.5) and (age >= 18 and age <= 60):
#         return True
#     elif (age < 18) and (18.5 < bmi < 24.5):
#         return True
#     elif (not health_condition) and (18.5 < bmi < 24.5) and (age > 60):
#         return True
#     else:
#         return False

# age = int(input())
# bmi = float(input())
# condition = input() == 'True'

# print(gym(age, bmi, condition))

# def loan_eligibility(age, income, score, debt):
#     if (25 <= age <= 65) and (income >= 50000) and (score >= 700) and (debt < 50000):
#         return True
#     elif (age < 25) and (income >= 70000) and (score >= 750) and (debt < 30000):
#         return True
#     elif (age > 65) and (income >= 40000) and (score >= 650) and (debt < 20000):
#         return True
#     else:
#         return False
    
# age = int(input())
# income = float(input())
# score = int(input())
# debt = float(input())

# print(loan_eligibility(age, income, score, debt))

# def fabricExcess(inches):
#     if inches % 36 == 0:
#         return 0
#     else:
#         return ((inches // 36) + 1) * 36 - inches
    
# inches = int(input())

# print(fabricExcess(inches))

# def isEquilateralTriange(a, b, c):
#     return a == b == c

# a = float(input())
# b = float(input())
# c = float(input())

# print(isEquilateralTriange(a, b, c))