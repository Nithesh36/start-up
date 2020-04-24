#lists are mutable(changeable) and list elements can be any type str,int,float
#we can also create a empty list use []
alist =  ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))
print(alist[0])#here the first element is printed because its index value is 0
r=(alist[3][0])
print(r)#accessing sublist elements using a index value here the index value of sublist 
#is [3] and we can easily access the  element os sublist [0]

#add element use slicing
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)#we also use the slicing to add a multiple items in a list


#remove value use slicing
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[2:3] = []
print(alist)#We can also remove elements from a list by assigning the empty list to them.

#Using slices to delete list elements can be awkward and therefore error-prone. Python provides an alternative that is more readable.
#The del statement removes an element from a list by using its position.

a = ['one', 'two', 'three']
del a[2]#its possible to del the specified index in the list use index value
print(a)
del a#here the all the elements in the list can deleted and the list also deleted
print(a)#NameError: name 'a' is not defined on line 5 because the list is deleted
del a[-7]#when use negative index ..it cause runtime error if the index is out of range 





#empty slicing
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']

alist[3:3]=['e']
print(alist)
#We can even insert elements into a list by squeezing them into
#an empty slice at the desired location.
#empty slice means there is no slicing happen when use same index value in start and end
#alist[4:4] = ['e']here the element can be insert at 4 position there is no slicing
a = [81, 82, 83]
b = a[:1]       # make a clone using slice
print(a == b)
print(a is b)
b[0] = 5
print(a)
print(b)

#there is one disadvantage ..is when we do not follow the order the values are moved to anpother location
