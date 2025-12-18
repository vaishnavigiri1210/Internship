#dictionary

d={'a':'apple','b':'banana'}
num={1:10,2:20,3:30}
a={1:100,2:200,3:300,'x':'data','y':50000}
print(d)
print(num)
print(a)
print(type(d))
print(type(num))
print(type(a))

#accesing dictionary only key not index
print(d['a'])
print(num[2])

#mutable
num[0]=000
print(num)

#using dict() function we can convert tuple into list
data=([1,23],[2,54],[3,65],[4,78])
x=dict(data)
print(x)
print(type(x))

#empty dictionary
abc={}
print(type(abc))
abc[1]='gpp'
abc[2]='xyz'
print(abc)

#methods
info={1:1000,2:2000,3:3000,4:4000,5:5000}
print(info.keys())      #returns list of key
print(info.values())    #returns list of values
print(info.items())     #returns list of key-value pairs (give in tuple form)
print(info.get(2,0))    #returns value of index 2 if available otherwise prints 0   (2000)
print(info.get(7,12))   #returns value of index 7 if available otherwise prints 12  (12)