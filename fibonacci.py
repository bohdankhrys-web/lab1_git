def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_list = [0, 1]
    
    for _ in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
        
    return fib_list

n_terms = int(input("How many Fibonacci numbers do you want? Enter a number: "))
print(f"First {n_terms} Fibonacci numbers: {fibonacci(n_terms)}")