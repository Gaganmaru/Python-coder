
list=[1,2,3,4,5,6,7,8,9,10]
#append
list.append(11)
print(list)
#remove
list.remove(3)
print(list)
#insertindex
print(list.index(4))
#ascendind
list.sort()
print(list)
#Descending
list.reverse()
print(list)
#sum of list
s=0
for sum in list:
    s+=sum
print(s) 
s=0
#average of list
for avg in list:
    s+=sum/2
print(s)  
#function for sum and average
def reverse(list):
   s=0
   for sum in list:
    s+=sum
   print(s)
    
   print(sum/2)
reverse(list)

#reverse list compherensive
r=list[::-1]
print(r)

#even num. square:
list2=[x**2 for x in range(21) if x%2==0]
print(list2)

#largest num. and smallest num. in list:
print(max(list))
print(min(list))

#count:
print(list.count(1))

#merge two lists:
print(list+list2)

#split list:
print(slice(list))

# #remove duplicates:
# list3=[1,2,2,3,4]
# for d in list:
#    if d is not in list3:
      



 



