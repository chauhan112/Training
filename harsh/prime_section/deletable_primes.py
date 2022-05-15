def prime_number_check(n):  # function for prime numbers
    if n > 1:
        for i in range(2, int(n / 2) + 1):  # 2 is minimum and n/2 is the highest divider for a integer number
            if n % i == 0:  #
                return False  # in case if the number is divisible with any number it will return False.
        return True  # if not divisible with any number return True therefore it is prime number.


import itertools


def isDeletablePrime(n, *, valor=True):
    if prime_number_check(n):
        N = str(n)
        S = len(N)
        if S > 1 and any(p in N for p in "2 3 5 7".split()):
            resul = list()
            for num in set(map(lambda x: int("".join(x)), itertools.combinations(N, S - 1))):
                # set(...) eliminate potencial duplicates like with 331 there are 2 way to get 31, removing the firts or second 3
                temp = isDeletablePrime(num, valor=True)
                if temp:
                    resul.extend((n,) + tt for tt in temp)
            if valor:
                return tuple(filter(lambda r: len(r) == S, resul))
            else:
                return any(len(r) == S for r in resul)
        elif n in {2, 3, 5, 7}:  # base case
            return ((n,),) if valor else True
    return tuple() if valor else False  # base case and default


print(3301, "->", isDeletablePrime(3301))
print(3793, "->", isDeletablePrime(3793))
print(1601, "->", isDeletablePrime(1601))
