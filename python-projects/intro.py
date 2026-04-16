print("hello world!")
# comment like //
'''
this is like 
/*
comment
*/
'''

# variables
x=100
y=5.5
x='hello'
print(x)
x=[1,2,3]

x=100
y=10
result=x//y
print(result)

minval=min([3,4,5,1,-1])
print(minval)
raised=pow(2,4)
raised=2**4

x=-1
y=1
if x<0:
    x+=10
if x>10 and y <5:
    print("help")
if x>6 or y < 10:
    print('yes')

if x > 10:
    x=9
elif x<10:
    x=11
else:
    x=0

lst=[1,2,3,4,5]
for i in range(5):
    print(i,lst[i])

for i in range(1,len(lst),2):
    print(i, lst[i])

for i, val in enumerate(lst):
    print(i, val)

for num in lst:
    print(num)

def hello():
    print("hello world!")

def greeting(name="Buddy"):
    print("hey", name)
hello()
greeting("Bob")
greeting()

demo="kathleen's email address is "
email="kathleen@gmail.com"

# A string is a list of characters
for c in demo:
    print(c)
for i,c in enumerate(demo):
    print(i, c)
last_char=email[-2]
print(last_char)

if "@" in email:
    print("yes it's an email address")

# string slicing
# slice email into username and domain
# allows for slicinng from start index to end index
# [start:end]
index=email.index("@")
print(index)
username=email[0:index]
domain=email[index+1:len(email)]
print(domain)






