# solve √a + √b = √n

# solve √a + √b = √2023 
# find a and b

# input (n)= 2023
# output (a,b) = [[0, 2023], [7, 1792], [28, 1575], [63, 1372], [112, 1183], [175, 1008],
# [252, 847], [343, 700], [448, 567], [567, 448], [700, 343], [847, 252], [1008, 175], 
# [1183, 112], [1372, 63], [1575, 28], [1792, 7], [2023, 0]]


import math

def calcB(a,n):
    return n-2*math.sqrt(n*a) + a


def solution(n):
    return [[a, int(calcB(a,n))] for a in range(0,n+1) if calcB(a,n).is_integer()]

# num = int(input("enter integer number: "))
# result = solution(num)
# print(result)


###### Way2 ####

def solution2(n):
    res = []

    for a in range(0,n+1):
        b = n-2*math.sqrt(n*a)+a
        if b.is_integer():
            res.append([a,int(b)])
        
    return res

sol2 = solution2(2023)
print(sol2)