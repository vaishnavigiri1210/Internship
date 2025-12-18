#list

a=[4,1,43,21,67,4,89,20,5,4,92,61,76]
print(a)
num=[10,20,30,40,50,60]
print(num)

#built in functions
print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))   #uses when only same datatype present

list('mnp')
print(list)
data=[0,0,0,0,False]
print(any(data))
b=[0,0,0,3,False]
print(any(b))
print(all(b))
print(all(a))

#built-in methods
print(a.index(5))
print(a.count(4))
print(a.append(0))          #appends element at end
print(a.insert(1,22))       #mutable
print(a.remove(5))
w=a.pop()
print(w)
print(a)
print(a.sort())
print(a.reverse())


#assigninng list elements
x,y,z=a[:3]
print(x)
print(y)
print(z)

#Slicing
print(num[2:4])
print(num[2:])
print(num[:5])
print(num[:])

#replacing set of elements
num[3:6]=['hello','world']
print(num)

#existence of element using 'in'
print(80 in num)
print('hello' in num)
print(40 not in num)

#Arithmetic Operations
print(num*2)
print(num +[4,8])

#iterating through list
#odd no
# for n in num:
#     if n % 2!=0:
#         print(n,end='')

#deleting elements
del num[2:5]
print(num)
# del num
# print(num)

#multi-dimensional list (list of list)
mat=[[1,2,3],[4,5,6],[7,[8,9]]]
print(mat)
print(mat[2])
print(mat[2][1])
print(mat[2][1][0])