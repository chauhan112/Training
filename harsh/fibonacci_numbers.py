class Fabonacci:

    #def __init__(self):
       # self.digit = digit

    def fabo_num(self, digit):
        #self.digit = digit
        #self.digit = digit
        if digit < 1:
            return -1
        if digit == 1:
            return 0
        if digit == 2 or digit == 3:
            return 1
        a = self.fabo_num(digit - 1)
        b = self.fabo_num(digit - 2)
        return a + b

    def fabo_num_2(self, digit):
        self.digit = digit
        print("n -> " + str(digit))
        print("self -> n -> " + str(self.digit))
        #self.digit = digit
        if self.digit < 1:
            return -1
        if self.digit == 1:
            return 0
        if self.digit == 2 or self.digit == 3:
            return 1
        print("!")
        a = self.fabo_num_2(self.digit - 1)
        b = self.fabo_num_2(self.digit - 2)
       # print(self.digit)
        return a + b


fabi = Fabonacci()
print(fabi.fabo_num(4))
print(fabi.fabo_num_2(4))
