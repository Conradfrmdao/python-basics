a=[1,2,3,4]
b=['apples','bananas','cherries']
c=['kampala',256,'uganda']
##acess list
print(a[2],b[0],c[0],c[2])
names=[]

b[1]='oranges'  # change value in list b    
print(b)
print("Updated list b:", b)

##add elements to list
c.append('Entebbe')
print("Updated list c:", c)

##adding multiple elements
c.extend([2,4,5])
print("Extended list c:", c)

## insert element at specific position
a.insert(1,235)
print("List a after insertion:", a)

## remove speciic element from list
a.remove(3)
print("List a after removing 3:", a)

## remove using del
del b[2]
print("List b after deletion:", b)

## pop last element from list
c.pop()
print("List c after popping last element:", c)