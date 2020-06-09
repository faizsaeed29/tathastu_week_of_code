def House(l):
  b = len(l)
  if (b == 2):
    return max(l)
  if (b == 1):
    return l[0]
  if (b == 3):
    return max(l[1],l[0]+House(l[2:]))
  return max(l[1],House(l[3:]),l[0]+House(l[2:]))
  
n = int(input("Enter the number of houses in a line : "))
l = []
for i in range (0,n):
  a = int(input("Enter the value in the house number"+str(i+1)+":"))
  l.append(a)
print ("The maximum stolen value from the Houses is",House(l))
