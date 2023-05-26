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
equations = 5  # Количество уравнений
variables = 5  # Количество переменных

# Создаем пустые списки для коэффициентов и правых частей
coefficients = []
right_hand_side = []
file = open("input.txt", "r",encoding='utf-8')

for i in range(equations):
    equation = file.readline()
    equation_parts = equation.split()

    # Считываем коэффициенты
    equation_coefficients = [float(equation_parts[j]) for j in range(variables)]
    coefficients.append(equation_coefficients)

    # Считываем правую часть
    equation_rhs = float(equation_parts[variables])
    right_hand_side.append(equation_rhs)

# Выводим полученные коэффициенты и правые части
print("Считанные коэффициенты:")
print(coefficients,right_hand_side)
file.close()

# Решение системы уравнений
x = gaussian_elimination(coefficients, right_hand_side)

x0 = [0, 0, 0, 0, 0] # Начальное приближение
xz = seidel(coefficients, right_hand_side, x0)
# Вывод результата
print("Решение системы:")
print(xz)

# загрузка в txt
letters = ['a','b','c','d','e']

file = open('answear_data.txt','w',encoding='utf-8')
file.write('Метод гаусса\n')
for i in range(0,len(x)):
    file.write(f'{letters[i]} = {x[i]}\n')

file.write('Метод Зейделя\n')
for i in range(0,len(xz)):
    file.write(f'{letters[i]} = {xz[i]}\n')
file.close()
# вычисление погрешности
error_rate = 0
k = 0
for i in range(0,len(x)):
    k = k + coefficients[0][i] * x[i]

error_rate = abs(right_hand_side[0] - k)
print('\nпогрешность гаусса:\n')
print(error_rate)
error_rate = 0
k = 0
for i in range(0,len(x)):
    k = k + coefficients[0][i] * xz[i]
error_rate = abs(right_hand_side[0] - k)
print('\nпогрешность Зейделя:\n')
print(error_rate)