n_1 = 0  
n_2 = 1  
count = 0  
max = int(input(" enter max number : "))
while n_1<max:  
    print(n_1)  
    nth = n_1 + n_2  
    n_1 = n_2  
    n_2 = nth  
    count += 1
print(f" Fibonacci numbers smaller than {max} : {count}")