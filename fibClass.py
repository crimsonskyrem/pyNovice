from memory_profiler import profile

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    # @profile
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        else:
            raise StopIteration
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

@profile
def iterTest(num):
    for n in Fab(num):
        print(n)

@profile
def listTest(num):
    res = fab(num)
    for n in res:
        print(n)



# listTest(10000)
iterTest(10000)