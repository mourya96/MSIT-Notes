def replaceString(s1, s2, s3):
    i = 0
    s = ''
    while i < len(s1):
        flag = True
        if s1[i] == s2[0]:
            for j in range(len(s2)):
                if s1[i+j] != s2[j]:
                    flag = False
            if flag:
                s = s + s3
                i = i + len(s2)
        else:
            s += s1[i]
            i = i + 1

    return s

string1 = input()
string2 = input()
string3 = input()

print(replaceString(string1, string2, string3))