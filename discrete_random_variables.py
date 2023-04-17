import math

from utils import comb, factorial


class HyperGeometric:
    def __init__(self, N, a, k):
        self.N = N
        self.a = a
        self.k = k

    def pmf(self, r):
        if self.k - r < 0:
            return 0
        else:
            return comb(self.a, r) * comb(self.N - self.a, self.k - r) / comb(self.N, self.k)


class Bernoulli:
    def __init__(self, p):
        self.p = p

    def pmf(self):
        return self.p


class Binomial:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, k):
        return comb(self.n, k) * (self.p**k) * ((1 - self.p) ** (self.n - k))


class Uniform:
    def __init__(self, n):
        self.n = n

    def pmf(self):
        return 1 / self.n


class Geometric:
    def __init__(self, p):
        self.p = p

    def pmf(self, k):
        return self.p * ((1 - self.p) ** (k - 1))


class Pascal:
    def __init__(self, p, n):
        self.n = n
        self.p = p

    def pmf(self, k):
        return comb(self.n - 1, k - 1) * (self.p**k) * ((1 - self.p) ** (self.n - k))


class LambdaPoisson:
    def __init__(self, lambd, k):
        self.lambd = lambd
        self.k = k

    def pmf(self, r):
        return ((self.lambd**r) / factorial(r)) * math.exp(-self.lambd)
