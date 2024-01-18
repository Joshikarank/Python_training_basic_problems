def prime_factorization(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i, end=' ')
    if n > 1:
        print(n)

number = int(input("Enter a number: "))
print("Prime factors:")
prime_factorization(number)