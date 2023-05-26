
def main():
    A = [[-310.0,4.5,17.0,4.5,-8.3],
         [-4.7,880.0,-7.7,-6.2,17.8],
         [4.8,12.1,-510.0,2.1,1.1],
         [9.8,9.8,-6.2,1.6],
         [-7.6,2.8,8.8,-2.8,260.0],
         ]
    b = [-1377.0,8076.6,286.4,132.0,-1212.6]
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
            ratio = A[j][i] / A[i][i]
            b[j] -= ratio * b[i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]

    # Обратный ход метода Гаусса
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= A[j][i] * x[i]

    return x
print(main())