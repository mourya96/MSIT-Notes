# def vowelCount(s):
#     count = 0
#     for c in s:
#         if c in 'aeiouAEIOU':
#             count += 1
#     return count

# print(vowelCount(input()))

# def replaceString(s1, s2, s3):
#     output = ''
#     i = 0
#     while i < len(s1):
#         if s1[i:i+len(s2)] == s2:
#             output += s3
#             i += len(s2)
#         else:
#             output += s1[i]
#             i += 1

#     return output

# s1 = input()
# s2 = input()
# s3 = input()

# print(replaceString(s1, s2, s3))
# def interleave(string1, string2):
#     output = ''
#     for i in range(len(string1)):
#         output = output + string1[i] + string2[i]
#     return output

# def interleaveTwoStrings(s1, s2):
#     m = len(s1)
#     n = len(s2)
#     output = ''
#     if m > n:
#         output += interleave(s1[:n], s2)
#         output += s1[n:]
#     elif m < n:
#         output += interleave(s1, s2[:m])
#         output += s2[m:]
#     else:
#         output += interleave(s1, s2)
#     return output

# print(interleaveTwoStrings(input(), input()))

# def rotateStringLeft(s, k):
#     n = len(s)
#     k = k % n
#     return s[k:] + s[:k]

# print(rotateStringLeft(input(), int(input())))

# def sameChars(s1, s2):
#     for c in s1:
#         if c not in s2:
#             return False
#     for c in s2:
#         if c not in s1:
#             return False
#     return True

# print(sameChars(input(), input()))

# def leastFrequentLetters(s):
#     s = s.lower()
#     output = ''
#     min_count = float('inf')
#     alphabets = 'abcdefghijklmnopqrstuvwxyz'
#     for c in alphabets:
#         count = s.count(c)
#         if count < min_count and c in s:
#             min_count = count
    
#     for c in alphabets:
#         count = s.count(c)
#         if count == min_count:
#             output += c
#     return output

# print(leastFrequentLetters(input()))

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    for c1 in s1:
        for c2 in s2:
            if s1.count(c2) == s2.count