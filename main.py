
# reduce() function is not a built-in function anymore ,and it can be found in the functools module

from functools import reduce
def add(x,y):
      return x+y

list =[2,3,4,5,6]
print(reduce(add,list))


# map() function -The map() function iterates through all items in the given iterable
#  and execute the function we passes as an argument on each of them
def starts_with_A(s):
      return s[0]=="A"

fruit =["Apple","Banana","pear","mango","Apricot"]
map_object =map(starts_with_A,fruit)
print(list(map_object))

#another example
def sq(a):
      return a*a
num =[2,3,4,5,6,7,8,9,]
square = list(map(sq,num))
print(square)



#filter() function forms a new list that contains only elements that satisfy a certain condition

def starts_with_A(s):
      return s[0]=="A"

fruit =["Apple","Banana","pear","mango","Apricot"]
filter_object =filter(starts_with_A,fruit)
print(list(filter_object))




#--------------------------MAP------------------------------
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

def sq(a):
    return a*a

num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)
num = [2,3,5,6,76,3,3,2]
square = list(map(lambda x: x*x, num))
print(square)


def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

#--------------------------FILTER------------------------------
list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
#--------------------------REDUCE------------------------------
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)












from array import*

# vals = array('i',[1,2,3,4,5,])
#
# for i in range(5):
#    print(vals[i])

# val =array('i',[2,3,4,5,])
# for i in range(4):
#    print(val[i])
val=array('i',[2,3,4,5,6,7])



val.reverse()
print(val)



  
