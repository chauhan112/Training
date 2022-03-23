def prime_number_check(n):  # function for prime numbers
    if n > 1:
        for i in range(2, int(n / 2)+1):  # 2 is minimum and n/2 is the highest divider for a integer number
            if n % i == 0:                #
                return False  # in case if the number is divisible with any number it will return False.
        return True  # if not divisible with any number return True therefore it is prime number.

def deletable_prime(n):
    if prime_number_check(n):       # First it should be checked if it is prime or not prime
        arr  = []
        while(n<=9):
           a =  n%10
           n = (n-a)/10
           arr.append(a)

         b = len(arr)
        sum = 0
        arr.remove()
         for i in range(b,0):
             sum += arr[b]*10

         sum += arr[0]


             






def number_of_ways(n):

