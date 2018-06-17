
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
a = []
b = 2
Vi_tri = -1
for i in range(len(c)):
    if b**c[i] <1025:
        Vi_tri = Vi_tri +1
        a.insert(Vi_tri, c[i])
print(*a, sep = ", ")