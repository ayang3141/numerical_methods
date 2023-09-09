from PolynomialEvaluator import PolyEvaluator
import numpy as np

if __name__ == '__main__':
    coefs = [1, 2, 5, 6, 3]
    evaluator = PolyEvaluator(coefs)

    print(f"Storing Powers: ", evaluator.storing_powers(0))
    print(f"Horner's Method: ", evaluator.horners_method(0))
