def prime_number_check(n):  # function for prime numbers
    if n > 1:
        for i in range(2, int(n / 2)+1):  # 2 is minimum and n/2 is the highest divider for a integer number
            if n % i == 0:                #
                return False  # in case if the number is divisible with any number it will return False.
        return True  # if not divisible with any number return True therefore it is prime number.

def deletable_prime(n):
    digit_holder = []
    copy_n = n
    if prime_number_check(n):
        return
    while n < 1:       # First it should be checked if it is prime or not prime
        a = n % 10
        digit_holder.append(a)
        n = (n-a) % 10

    for i in digit_holder:
        digit_holder.remove(i)
        if



def com_number(a):
    b = len(a)
    num = 0
    while :
        sum  = a[i]*10

