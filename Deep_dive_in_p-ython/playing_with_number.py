import math
X= "5"
#print(type(X)) #<class 'str'>
#print(X*5) #55555

#Now we convert this string into real number 

x_int= int(X)
#print(type(x_int))  # int
#print(x_int*5) #25

#Rounding , Truncate , floor ,ceil
price = 35.54899367

print(round(price))


print(math.trunc(price))

print(math.floor(price))

print(math.ceil(price))