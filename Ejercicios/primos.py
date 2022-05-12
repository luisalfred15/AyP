number = int(input('Please enter a number to verify if it is prime: '))
aux = 0                             # 'aux' will count how many dividers have 'number'

if number < 0:
    print('Please enter a valid number')
else:
    for i in range(1,number+1):
        if number % i == 0:
            aux += 1                # When found a divisor of 'number', 'aux' will count it

if aux == 2:                        # Since primes only have two divisors, 1 and themselves, when 'aux' is 2, then 'number' is prime
    print(number,'is prime')
else:
    print(number,'is not prime')