import numpy as np

class FunctionSolver():
    """
    Class for solving functions
    """
    def __init__(self, tolerance, function):
        self.tol = tolerance
        self.func = function

    def bisection_method(self, interval: np.ndarray):
        """
        Bisection method to solve f(x) = 0 in a given interval

        :param interval: interval [a, b] in which to search for root
        :return: the approximated root of the function
        """
        # Check if interval is valid length
        assert len(interval) == 2, "invalid interval"

        interval = np.sort(interval)
        a, b = interval[0], interval[1]
        f_a, f_b = self.func(interval)

        # Check if root even exists in interval
        assert f_a * f_b < 0, "Either no root exists, or too big of interval"

        # do bisection
        while (b-a)/2.0 > self.tol: # while c is not close enough to the root
            c = (a + b)/2.0
            f_c = self.func(c)

            if f_c == 0:
                return c
            elif np.sign(f_a) * np.sign(f_c) < 0: # if root is in [a, c] ...
                b = c
            else: # if root is in [c, b] ...
                a = c
                f_a = f_c

        return (a + b)/2.0

    def fixed_point_iteration(self, guess: float, num_iter: int):
        """
        Fixed Point iteration to solve f(x) = x
        :param guess: initial guess for x
        :param num_iter: number of iterations to run the fixed-point calculations
        :return: approximate solution x
        """
        x = guess
        for i in range(num_iter):
            f_x = self.func(x)
            x = f_x
        return x

