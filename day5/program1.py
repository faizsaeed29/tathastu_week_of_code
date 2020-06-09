def replace1(n):
  a = int(str(n).replace('0','5'))
  return (a)


n = int(input("Enter the number you want to check :"))
print ("The number after replacing all 0 with 5 will be : ",replace1(n))
