def prime_check(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
            print("it is a prime")
    else:
            print("it is not prime")


prime_check(7)