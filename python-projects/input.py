num=input('Enter a number')
print("You entered",num)
#num+=1
num=int(input('Enter a number'))

with open("movies.txt") as file:
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    height_dict={}
    for line in file:
        line=line.strip()
        values=line.split()
        values=[int(x) if x.isnumeric() else x for x in values]
        height_dict[values[0]+" "+values[1]]=int(values[2])
        print(height_dict)