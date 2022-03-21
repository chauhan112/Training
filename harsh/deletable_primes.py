def prime_number_check(n):  # function for prime numbers
    if n > 1:
        for i in range(2, int(n / 2)):  # 2 is minimum and n/2 is the highest divider for a integer number
            if n % i == 0:                #
                return False  # in case if the number is divisible with any number it will return False.
        return True  # if not divisible with any number return True therefore it is prime number.

def deletable_prime(n):
    