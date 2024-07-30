zero = 0
one = 0

def fibonacci(n):
    if n == 0 :
        zero+=1
        #print("0", end= " ")
        return 0
    
    elif n == 1 :
        one+=1
        #print("1" , end=" ")
        return 1
    
    else :
        return fibonacci(n-1) + fibonacci(n-2)

x = int(input())

for i in range(x):
    num = int(input())

    fibonacci(num)

    print(zero, one)

    zero = 0
    one = 0

