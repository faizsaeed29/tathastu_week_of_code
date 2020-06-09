def replace(l):
  for i in range (0,n-1):
    l[i] = max(l[i+1:])
  return (l)



n = int(input("Enter the size of the list :"))
l = []
for i in range (0,n):
  a = int(input("Enter the element number"+str(i+1)+"in the list :"))
  l.append(a)
print ("The list after replacing every element with greatest element on right side is :  ",replace(l))
