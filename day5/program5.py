def sort1(l):
  o = []
  e = []
  for i in l:
    if (i % 2 == 0):
      e.append(i)
    else:
      o.append(i)
  return sorted (o,reverse = True) + sorted(e)



n = int(input("Enter the number of elements you want to add in array : "))
l = []
for i in range (0,n):
  a = int(input("Enter the element number "+str(i+1)+" in the list: " ))
  l.append(a)
print ("The list of numbers after sorting them about giving condition is : ",str(sort1(l))[1:-1])
