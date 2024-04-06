# This program was made to get the first 100 prime numbers

# Having noticed that a prime number is only divisible by the unit and itselft
    
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
not_prime = []

print(f'Numbers to be evaluated: {random_numbers}')

for num in random_numbers:
    if num == 1:
        continue
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_prime.append(num)
                # print(f'{num} is not a prime number')
                break

prime_numbers = list(set(random_numbers) - set(not_prime))

if not prime_numbers:
    print(f'The list {random_numbers} does not contain prime numbers.')
else:
    print(f'The prime numbers in the list are: {prime_numbers}')
