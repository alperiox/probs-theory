import math


class Uniform:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pmf(self):
        return 1 / (self.b - self.a)


class Normal:
    def __init__(self, mu, sigma):
        if sigma < 0:
            raise "The variable `sigma` cannot be negative"
        self.mu = mu
        self.sigma = sigma

    def pmf(self, x):
        return 1 / math.sqrt(2 * math.pi * self.sigma) * math.exp(-((x - self.mu) ** 2) / (2 * self.sigma**2))


class Exponential:
    def __init__(self, lambd):
        self.lambd = lambd

    def pmf(self, r):
        if r < 0:
            return 0
        return self.lambd * math.exp(-self.lambd * r)


class Gamma:
    def __init__(self, lambd, u):
        self.u = u
        self.lambd = lambd
        self.gamma_u = math.gamma(u)

    def pmf(self, x):
        if x < 0:
            return 0
        return self.lambd * (self.lambd * x) ** (self.u - 1) * math.exp(-self.lambd * x)
