#리스트의 가장 작은 수,가장 큰 수,합계구하기 32~36p 
a=[38,21,53,62,19]
smallest=a[0]
for i in a:
    if i < smallest:
        smallest=i
print(smallest)

a=[38,21,53,62,19]
largest=a[0]
for i in a:
    if i > largest:
        largest=i
print(largest)

a=[38,21,53,62,19]
a.sort()
print(a[0],"and",a[-1])

a=[38,21,53,62,19]
min_value = min(a)
max_value = max(a)
print(min_value,"and",max_value)

a=[38,21,53,62,19]
result=0
for i in a:
    result += i
print(result)

a=[38,21,53,62,19]
result = sum(a)
print(result)

#리스트 표현식 사용하기 37~42p

a = [i for i in range(10)]
b= list(i for i in range(10))
print(a)
print(b)

a = [i + 5 for i in range(10)]
b= list(i * 2 for i in range(10))
print(a)
print(b)

a = [i for i in range(10) if i % 2 ==0]
print(a)

a = [i + 5 for i in range(10) if i%2 ==1]
print(a)

a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

a = [i * j for j in range(2,10)
           for i in range(1,10)] #얘는 걍 들여쓰기
print(a)

#리스트에 map 사용하기 43~45p

a = [1.2, 2.5,3.7, 4.6]
a = list(map(int,a))
print(a)

a = list(map(str,range(10)))
print(a)

a = list(map(int, input().split()))
print(a)

#튜플 응용하기 46~50p

a=(38,21,53,62,19,53)
b= a.index(53)
print(b)

a =(10,20,30,15,20,40)
b = a.count(20)
print(b) 

a = (38,21,53,62,19)
for i in a:
    print(i, end=' ')

a = tuple(i+5 for i in range(10) if i%2 == 1)
print(a)

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int,a))
print(a)

a = (38,21,53,62,19)
print(min(a), max(a), sum(a))

#2차원 리스트 사용하기
#2차원 리스트를 만들고 요소에 접근하기 56~57p

a=[[10,20],[30,40],[50,60]]
b=[[10,20],
   [30,40],
   [50,60]]
print(a)
print(b)

a=[[10,20],
   [30,40],
   [50,60]]
print(a[1][0])
print(a[0][1])

a[2][1] = 100
print(a)

#반복문으로 2차원 리스트 요소를 모두 출력하기 58~59p

a=[[10,20],
   [30,40],
   [50,60]]
for x,y in a:
    print(x,y)

a=[[10,20],
   [30,40],
   [50,60]]
for x in a:
    print(x)
    for y in x:
        print(y, end=' ')
    print()