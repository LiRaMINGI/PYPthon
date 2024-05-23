import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Параметры по умолчанию
x = np.linspace(0, 10, 500)
freq1 = 1.0
amp1 = 1.0
freq2 = 2.0
amp2 = 0.5

# Функция для генерации сигнала
def generate_signal(freq, amp):
    return amp * np.sin(2 * np.pi * freq * x)

# Создание окон
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))

# Первое окно: волна 1
line1, = ax1.plot(x, generate_signal(freq1, amp1), label='Волна 1')
ax1.set_xlabel('Время')
ax1.set_ylabel('Амплитуда')
ax1.set_title('Волна 1')
ax1.legend()

# Слайдер для частоты волны 1
axfreq1 = plt.axes([0.1, 0.05, 0.8, 0.03])
freq_slider1 = Slider(axfreq1, 'Частота 1', 0.1, 5.0, valinit=freq1)

# Слайдер для амплитуды волны 1
axamp1 = plt.axes([0.1, 0.01, 0.8, 0.03])
amp_slider1 = Slider(axamp1, 'Амплитуда 1', 0.1, 2.0, valinit=amp1)

# Второе окно: волна 2
line2, = ax2.plot(x, generate_signal(freq2, amp2), label='Волна 2')
ax2.set_xlabel('Время')
ax2.set_ylabel('Амплитуда')
ax2.set_title('Волна 2')
ax2.legend()

# Слайдер для частоты волны 2
axfreq2 = plt.axes([0.1, 0.25, 0.8, 0.03])
freq_slider2 = Slider(axfreq2, 'Частота 2', 0.1, 5.0, valinit=freq2)

# Слайдер для амплитуды волны 2
axamp2 = plt.axes([0.1, 0.21, 0.8, 0.03])
amp_slider2 = Slider(axamp2, 'Амплитуда 2', 0.1, 2.0, valinit=amp2)

# Третье окно: результирующая волна
line3, = ax3.plot(x, generate_signal(freq1, amp1) + generate_signal(freq2, amp2), label='Сумма')
ax3.set_xlabel('Время')
ax3.set_ylabel('Амплитуда')
ax3.set_title('Сумма волн')
ax3.legend()

# Обновление графиков при изменении значений слайдеров
def update(val):
    freq1 = freq_slider1.val
    amp1 = amp_slider1.val
    freq2 = freq_slider2.val
    amp2 = amp_slider2.val

    line1.set_ydata(generate_signal(freq1, amp1))
    line2.set_ydata(generate_signal(freq2, amp2))
    line3.set_ydata(generate_signal(freq1, amp1) + generate_signal(freq2, amp2))

    fig.canvas.draw_idle()

freq_slider1.on_changed(update)
amp_slider1.on_changed(update)
freq_slider2.on_changed(update)
amp_slider2.on_changed(update)

plt.show()