def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 4
results = factorial(number)
print(f"The facorial of {number} is {results}.")
