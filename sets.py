my_set={1,2,3,4,5}
empty_set=set()  # create an empty set
set1={1,2,1,3,3,1,2,4,2,3,5,2}
print("Set doesnt have duplicates:", set1)
set1.remove(2)  
print("Set after removing an element:", set1)

set1.add(6)  # add an element to the set
print("Set after adding an element:", set1)

b={1,2,3}
c={'b','c','d'}
b.union(c) # union of two sets
print("Union of b and c:", b.union(c))

x={'a','b','c'}
y={1,2,3,'c','b'}
z={2,4,'b'}

xUyUz=x.union(y).union(z)  # union of multiple sets
print("Union of x, y, and z:", xUyUz)
xNyNz=x.intersection(y).intersection(z) # intersection of multiple sets
print("Intersection of x, y, and z:", xNyNz)
