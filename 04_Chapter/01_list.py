# In python List is a datatype used to store set / collection of data of various data types
# List is similar to Arrays enclosed within square brackets
my_list = [2,"cat",True] # stored multiple datatypes in list

# List Indexing
# List elements can be accessed with indexes
print(f'Entire list is \n{my_list}')
item_list = ["city",34,False,"Stacy"]
print(item_list[1])
print(item_list[1:])

# List Methods
# There are many list methods in Python that allow use to modify, add, update, delete and do other operations in List
# List is mutable

# For e.g we have a list of unsorted intergers
demo_list = [3,2,3,43,23,54,12,54,3,5,32,12,5457,65]
demo_list.sort() # if want desc. sorting then we can pass the reverse = True
print(demo_list) # printed list in sorted format ~ asc in default. for desc. we need to pass the reverse = True

# reverse() method in Python
demo_list1 = [3,2,3,43,23,54,12,54,3,5,32,12,5457,65]
demo_list1.reverse()
print(demo_list1)

# append() method to add new element to last of the list
demo_list1.append(12321)
print(demo_list1) # got appended to the last of the list

# insert() method allows us to insert the desired element to the exact index in the list
# edge cases if passed index is out of range 
# if out of range and negative then the elements gets added to the head / first of the list
# if out of range and positive index then the element gets appended to the last of the list
demo_list3 = [3,2,3,43,23,54,12,54,3,5,32,12,5457,65]
demo_list3