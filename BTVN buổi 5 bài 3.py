

import math
x = []
for i in range(5):
    So = int(input("Nhap phan tu cua mang "))
    x.insert(i, So )
print(*x, sep = ", ")
y = []
for i in range(len(x)):
    Phantu_y = 3.14/2 - x[i]
    y.insert(i, Phantu_y)
print(*y, sep = ", ")
z=[]
for i in range(len(x)):
    Phantu_z = math.cos(x[i]) - math.sin(x[i])
    z.insert(i,Phantu_z)
print(*z, sep = ", ")
Tong = 0
for i in range(len(z)):
    Tong = Tong + z[i]
print(Tong)