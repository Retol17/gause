import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def gaussian_elimination(A, b):
    n = len(A)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск наибольшего элемента в столбце
        max_idx = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_idx][i]):
                max_idx = j

        # Перестановка строк
        A[i], A[max_idx] = A[max_idx], A[i]
        b[i], b[max_idx] = b[max_idx], b[i]

        # Приведение к треугольному виду
        for j in range(i + 1, n):
            lcm_denominator = lcm(A[i][i], A[j][i])
            ratio1 = lcm_denominator // A[i][i]
            ratio2 = lcm_denominator // A[j][i]

            for k in range(i, n):
                A[j][k] = A[j][k] * ratio2 - A[i][k] * ratio1
            b[j] = b[j] * ratio2 - b[i] * ratio1

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i] -= A[i][j] * x[j]
        x[i] = b[i] / A[i][i]

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

# Решение системы уравнений
x = gaussian_elimination(A, b)

# Вывод результата
print("Решение системы:")
for i, value in enumerate(x):
    print(f"x{i + 1} = {value}")