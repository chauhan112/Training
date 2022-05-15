from random import randint
import math
class IPrimeChecker:
     def check(self,val:int):
            raise NotImplementedError("abstract method") 
class NormalWay(IPrimeChecker):
    def check(self,n:int):
        if n > 1:
            for i in range(2, int(math.sqrt(n))+1):
                # 2 is minimum and n/2 is the highest divider for a integer number
                 if n % i == 0:
                    return False
                    # in case if the number is divisible with any number it will return False.
            return True
            # if not divisible with any number return True therefore it is prime number.
        return False

class FermatWay(IPrimeChecker):
    def power(self,a, n, p):
        res = 1
        # Update 'a' if 'a' >= p
        a = a % p
        while n > 0:
        
            # If n is odd, multiply
            # 'a' with result
            if n % 2:
                res = (res * a) % p
                n = n - 1
            else:
                a = (a ** 2) % p
                # n must be even now
                n = n // 2
        return res % p
    def check(self,num3:int):
        if num3 < 2:
            return False
        if num3==2 or num3==3:
            return True
        c= 0
        for i in range(5):
            a = randint(2, num3-1)  
            if self.power(a, num3-1, num3)!= 1:
                c += 1
            if c > 2 : 
                return False
        return True

class OldWay(IPrimeChecker):
    def check(self,n):  # function for prime numbers
        if n > 1:
            for i in range(2, int(n / 2)+1):  
                # 2 is minimum and n/2 is the highest divider for a integer number
                if n % i == 0:               
                    return False            
                # in case if the number is divisible with any number it will return False.
            return True                    
        # if not divisible with any number return True therefore it is prime number.

class Dprime:
    def __init__(self):
        self.set_prime_checker(NormalWay())
        
    def deletable_prime(self,num):


        if self._checker.check(num): # it puts self to the _checker.check method and check that function
            temp = self.number_to_list(num)
            temp_length = len(temp)
            #print("outter -> "+ str(sun))

            #print(num)
            for i in range(0, temp_length):
                get_del = self.delete_number(temp, i + 1)
                get_num = self.com_number(get_del)
                if self._checker.check(get_num):
                    #print(get_num)
                    if get_num == 2 or get_num == 3 or get_num == 5 or get_num == 7:
                            self.mal += 1
                           # print(self.mal)
                    else:
                        self.deletable_prime(get_num)
        return self.mal
    
    def delete_number(self,l, pos):
        pos = pos - 1
        c_list = []
        l_len = len(l)
        for i in range(0, l_len):
            if i != l_len - pos - 1:
                c_list.append(l[i])
        return c_list


    def com_number(self,a):
        if len(a) ==0:
            return 0
        g = a.copy()
        g.reverse()
        return int("".join([str(i) for i in g]))

    def number_to_list(self,num):
        f = []
        while num > 0:
            a = num % 10
            f.append(a)
            num = (num - a) / 10
        length = len(f)
        for i in range(0, length):
            f[i] = int(f[i])
        return f
    
    def set_prime_checker(self,checker:IPrimeChecker):
        self._checker = checker
        self.mal = 0   
        
class Main: 
    def deletableprime(n,way = FermatWay()):
        #n = 537499093
        #n = 46216567629137
        d = Dprime()
        d.set_prime_checker(way)  
        cde = d.deletable_prime(n)
        return cde
       
class TestCase:
    def example1():
        n = 46216567629137
        out =  Main.deletableprime(n)
        assert out ==121
        print(out)
    
        

#TestCase.example1()  