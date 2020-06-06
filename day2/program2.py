n = int(input("Enter the value of n: "))
a = 0
b = 1
print("The Fibonacci series upto", n, "th number is following:")
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
