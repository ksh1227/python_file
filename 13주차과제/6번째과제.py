#39
def a(n):
    for i in range(n + 1):
        if i % 2 != 0:
            print(i, end=' ')

b = int(input())
a(b)

#40
def a(n):
    if n % 3 == 0:
        print(n)

b = int(input())
a(b)

#41
def a(n1, n2, n3, n4):
    return max(n1, n2, n3, n4), min(n1, n2, n3, n4)

b, c, d, e = map(int, input().split())
m1, m2 = a(b, c, d, e)
print(m1, m2)

#42
def a(n):
    for i in range(n + 1):
        if i % 2 != 0:
            print(i, end=' ')

b = int(input())
a(b)

#43
def a(n):
    c = 1
    for i in range(1, n + 1):
        c *= i
    print(c)

b = int(input())
a(b)

#44
def a(n, m):
    d = 0
    for i in range(n, 10):
        for j in range(m, 10):
            if i * j >= 30:
                d += i * j
    print(d)

b, c = map(int, input().split())
a(b, c)

#45
def a(lst):
    print(sum(lst))

b = [1, 2, 3, 4, 5]
a(b)