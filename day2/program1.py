def Prime(N):
    a = 2
    b = N // 2
    while b >= a:
        if N % a == 0:
            return False
        a += 1
        b = N // a
    return True

def Palindrome(n):
    N = str(n)
    L = len(N)
    for i in range(L // 2):
        if N[i] != N[L - 1 - i]:
            return False
    return True

def Odd(n):
    if n % 2 == 0:
        return False
    return True

def Armstrong(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False

def check():
    Number = int(input("Enter the number: "))
    if(Prime(Number)):
        print(Number, "is a prime number")
    if(Odd(Number)):
        print(Number, "is an odd number")
    else :
        print(Number, "is an even number")
    if(Palindrome(Number)):
        print(Number, "is a palindrome number")
    if(Armstrong(Number)):
        print(Number, "is an armstrong number")

check()
