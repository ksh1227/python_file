#11
a = list(map(int, input().split()))
b = input()
a.append(b)
print(a)

#12
a = list(map(int, input().split()))
del a[-2:]
print(a)

#13
a = list(map(int, input().split()))
for b, c in enumerate(a, start=101):
    print(b, c)

#14
a = [10, 20, 30, 40, 20, 10]
print(a.count(20))

#15
a = list(map(int, input().split()))
print(min(a), max(a))

#16
a = list(map(int, input().split()))
b = sum(a) - min(a) - max(a)
print(b)

#17
a = [10, 20, 30, 40, 20, 10]
b = [i for i in a if i != 20]
print(b)

#18
a = [i for i in range(1, 6)]
print(a)

#19
a = [i for i in range(1, 21) if i % 2 == 1]
print(a)

#20
a, b = map(int, input().split())
c = [2**i for i in range(a, b + 1)]
del c[-2]
del c[1]
print(c)

#21
a = input()
b = a.replace('Hello', 'Hi')
print(b)

#22
a = input().split()
b = '/'.join(a)
print(b)

#23
a = input()
b = a.lower().rjust(10)
print(b)

#24
a = list(map(int, input().split(';')))
a.sort(reverse=True)
for b in a:
    print(str(b).rjust(9))
