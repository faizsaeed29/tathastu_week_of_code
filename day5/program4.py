def knapsack(w,l):
  if (w == 0 or len(l) == 0):
    return 0
  if (len(l) == 1):
    if (l[0][0] > w):
      return 0
    return l[0][1]
  if (l[0][0] > w):
    return knapsack(w,l[1:])
  return max(l[0][1]+knapsack(w-l[0][0],l[1:]),knapsack(w,l[1:]))
  


n = int(input("Enter number of items you want to enter : "))
l = []
for i in range (0,n):
  w = int(input("Enter the weight for item number"+str(i+1)+": "))
  v = int(input("Enter the value for item number"+str(i+1)+": "))
w = int(input("Enter the value of weight capacity: "))
print ("The maximum value for the given weight value pair is : ",knapsack(w,l))
