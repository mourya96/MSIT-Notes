# def alternatingSum(l):
#     alt_sum = 0
#     for i in range(len(l)):
#         alt_sum += (-1)**(i % 2)*(l[i])
#     return alt_sum

# l = []

# for i in range(int(input())):
#     l.append(int(input()))

# print(alternatingSum(l))

# def isPalindromicList(l):
#     return l == l[::-1]

# l = []

# for i in range(int(input())):
#     l.append(float(input()))

# print(isPalindromicList(l))

# def vectorSum(a, b):
#     summed_list = []
#     for i in range(len(a)):
#         summed_list.append(a[i] + b[i])
#     return summed_list

# a = []
# b = []

# for i in range(int(input())):
#     a.append(int(input()))

# for j in range(int(input())):
#     b.append(int(input()))

# print(vectorSum(a, b))

def smallestDifference(l):
    if len(l) < 2:
        return -1
    l = sorted(l)
    diff = float("inf")
    for i in range(len(l)-1):
        d = abs(l[i+1] - l[i])
        if diff > d:
            diff = d
    return diff

l = list(map(int, input().strip().split(" ")))

print(smallestDifference(l))

# def dotProduct(a, b):
#     dot_prod = 0
#     if len(a) > len(b):
#         for i in range(len(b)):
#             dot_prod += a[i]*b[i]
#     else:
#         for i in range(len(a)):
#             dot_prod += a[i]*b[i]
#     return dot_prod

# a = []
# b = []

# for i in range(int(input())):
#     a.append(int(input()))

# for j in range(int(input())):
#     b.append(int(input()))

# print(dotProduct(a, b))