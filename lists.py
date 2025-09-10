#an empty list
my_list=[]
print(my_list)

#appending elements
my_list.append(10)
my_list.append(20) 
my_list.append(30) 
my_list.append(40) 
print(my_list) 

my_list=[10,20,30,40]

#insert 15 at the second position
my_list.insert(1,15)
print(my_list)


my_list=[10,20,30,40]
list=[50,60,70]
#extend list with another list

my_list.extend(list)
print(my_list)

my_list=[10,20,30,40,50,60,70]

#remove the last element
my_list.pop()

print(my_list)

my_list=[10,20,30,40,50,60,70]
#sort in ascending order

my_list.sort()

print(my_list)

my_list=[10,20,30,40,50,60,70]

#find index of value 30
index_30= my_list.index(30)

print(index_30)