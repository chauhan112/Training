class Fabonacci:

    def __init__(self, n_dight):
        self.n_dight = n_dight

    def fabo(self, n_dight):
        self.n_dight = n_dight
        if self.n_dight == 1 :
            return 0
        if self.n_dight <= 3 :
            return 1
        return self.fabo(self.n_dight-1) + self.fabo(self.n_dight-2)


fabi = Fabonacci(34)
print(fabi.fabo(34))