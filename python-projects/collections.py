a=[10,20,30,40]
a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(40)
print(a)
a.pop(2)
print(a)
a.pop()
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a=a[1:]
print(a)
a.append(5)
num=a.count(5)
print(num)
index=a.index(5)
print(index)
print(a)
a2=a
a2[1]=99
print(a)
a3=a[:]
a3[0]=99
print(a3)
print(a)

empty=[]
for val in a:
    empty.append(val)
empty[0]=1000
print(empty,a)
empty=[0]*5
empty[0]=1
print(empty)

squares=[]
for i in range(5):
    squares.append(i*i)
print(squares)

squares=[i*i for i in range(5)]
print(squares)
pets=['dog','cat','turtle','hermit crab']
dogs=[animal for animal in pets if animal=='dog']
leng={len(pet) for pet in pets}
print(leng)

s=set()
s={1,2,3}
s.add(1)
print(s)

dups=[1,2,3,3,3,3]
dups=set(dups)
print(dups)

fav_foods={'kath':'pizza','steve':'burger','john':'ribs'}
print(fav_foods)
food=fav_foods.get("dan")
#food=fav_foods['dan']

for key,value in fav_foods.items():
    print(key,value)

if 'dan' in fav_foods:
    print(fav_foods['dan'])
else:
    fav_foods['dan']='pizza'
print(fav_foods)