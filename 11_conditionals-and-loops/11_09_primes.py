# Print out every prime number between 1 and 1000.

for num in range(1,1001):
    if num > 1:
        for prim_div in range(2, int(num/2)+1):
            if (num % prim_div) == 0:
                break
    else:
        print(f"{num} is a prime number...")
        
