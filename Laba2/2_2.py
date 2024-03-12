def draw_sierpinski_triangle(n):
    # Функция для отрисовки треугольника Серпинского
    def draw_triangle(x, y, size):
        if size == 1:
            # Базовый случай - рисуем звездочку
            canvas[y][x] = '*'
        else:
            # Рекурсивно рисуем 3 меньших треугольника
            draw_triangle(x, y, size // 2)
            draw_triangle(x + size // 2, y, size // 2)
            draw_triangle(x + size // 4, y + size // 2, size // 2)

    # Создаем пустой холст
    size = 3 * (2 ** (n - 1))
    canvas = [[' ' for _ in range(size)] for _ in range(size)]

    # Начинаем отрисовку
    draw_triangle(0, 0, size)

    # Выводим результат
    for row in canvas:
        print(' '.join(row))

n = 4  # Количество итераций (минимум 3)
draw_sierpinski_triangle(n)
