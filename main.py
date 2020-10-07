import numpy as np
import sympy as sp

def main():
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    # z = np.array([[1,2], [3,4]])
    # print(np.add(x, y))
    # print(np.subtract(x, y))
    # print(np.multiply(2, x))
    # print(np.dot(x, y))
    # print(np.sum(x))
    # print(np.sum(x, axis=0))
    # print(np.sum(x, axis=1))
    # print(x.T)
    # print(np.matrix(x).H)
    # print(np.linalg.matrix_rank(x))
    # print(np.linalg.det(x))
    # A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
    # B = np.array([25, -10, -4])
    # print(np.linalg.solve(A,B))

    # x, y, z = sp.symbols('x y z')
    # res = sp.solve([sp.Eq(1 * x + 1 * y + 1 * z, 0),
    #                 sp.Eq(1 * x + 4 * y + 10 * z, 3),
    #                 sp.Eq(2 * x + 3 * y + 5 * z, 1)],
    #                [x, y, z])
    # print(res)

    # x, y = sp.symbols('x y')
    # res = sp.solve([sp.Eq(1 * x - 4 * y, 0),
    #                 sp.Eq(1 * x - 4 * y , 3)],
    #                [x, y])
    # print(res)

if __name__ == '__main__':
    main()

