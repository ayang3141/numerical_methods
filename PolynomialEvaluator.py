import numpy as np

class PolyEvaluator():
    """
    Polynomial Evaluator for a0 + a1*x + a2*x^2 + ... + an*x^n
    """
    def __init__(self, poly_coefs):
        # coefficients in form [a0 a1 a2 ... an]
        self.poly_coefs = poly_coefs

    def horners_method(self, x: float):
        """
        Horner's Method of Nested Multiplications
        a0 + x(a1 + x(a2 + x(a3 + ... (a_n-1 + x(a_n)))))
        :param x: input value
        :return: output of function at x
        """
        prev_accum = self.poly_coefs[-1]
        num_iter = len(self.poly_coefs) - 1 # number of a + x(prev) iterations
        for i in range(num_iter, 0, -1):
            prev_accum = self.poly_coefs[i-1] + x * prev_accum
        return prev_accum

    def storing_powers(self, x: float):
        """
        Storing Powers:
        :param x: input value
        :return: output of function at x
        """
        accum = 0
        x_power = 1
        num_iter = len(self.poly_coefs)
        for i in range(num_iter):
            accum += self.poly_coefs[i] * x_power
            x_power = x_power * x
        return accum