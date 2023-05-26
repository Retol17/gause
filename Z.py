import math


def dot_product(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))
def seidel(A, b, x0, epsilon=0.0001, max_iterations=100):
    n = len(A)
    x = x0.copy()


    for iteration in range(max_iterations):
        x_new = x.copy()

        for i in range(n):
            sigma1 = dot_product(A[i][:i], x_new[:i])
            sigma2 = dot_product(A[i][i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sigma1 - sigma2) / A[i][i]

        if max(abs(x_new[i] - x[i]) for i in range(n)) < epsilon:
            return x_new

        x = x_new

    return x

# Пример использования

# Коэффициенты системы уравнений
A = [[170.0, -3.8, 6.2, 7.7, -8.9],
     [-7.9, -950.0, 8.3, 8.1, -1.6],
     [3.4, 5.6, -910.0, -9.8, -1.1],
     [-0.7, 2.0, 9.8, -520.0, 7.0],
     [2.7, -9.4, 2.6, -3.8, 660.0]]

# Вектор правой части
b = [-4209.32, -11663.70, -4759.71, 11684.55, -12523.93]

# Начальное приближение
x0 = [0, 0, 0, 0, 0]

# Решение системы уравнений
x = seidel(A, b, x0)

# Вывод результата
print("Решение системы:")
for i, value in enumerate(x):
    print(f"x{i+1} = {value}")