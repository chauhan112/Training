def prime_number_check(n):  # function for prime numbers
    if n > 1:
        for i in range(2, int(n / 2)):  # 2 is minimum and n/2 is the highest divider for a integer number
            if n % i == 0:                #
                return False  # in case if the number is divisible with any number it will return False.
        return True  # if not divisible with any number return True therefore it is prime number.


print(prime_number_check(3))
print(prime_number_check(33))
print(prime_number_check(17))
print(prime_number_check(34))
print(prime_number_check(45))
print(prime_number_check(89))
print(prime_number_check(101))
print(prime_number_check(5))

for k in range(1000):
    if prime_number_check(k):
        print(k)
