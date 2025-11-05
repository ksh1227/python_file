#25
a = input().split()
b = list(map(int, input().split()))
c = dict(zip(a, b))
del c[a[0]]
del c[a[3]]
print(c)

#26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(park['english'], park['science'])

#27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
kim = dict.fromkeys(kim, 100)
print(kim)

#28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
if 'english' in lee:
    lee.pop('english')
print(lee)

#29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
for b, c in lim.items():
    print(b, c)

#30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
b = {b: c for b, c in choi.items() if c >= 90}
print(b.keys())

#31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
b = yoo.values()
c = sum(b) / len(b)
print(c)