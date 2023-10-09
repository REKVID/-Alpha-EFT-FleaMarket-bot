import pyautogui
import cv2
import numpy as np
import keyboard

# Загрузка изображения
template = cv2.imread('image.png', 0)
h, w = template.shape[:2]

# Бесконечный цикл для ожидания нажатия на бинд
while True:
    keyboard.wait('y')
    # Ожидание нажатия на бинд
    #pyautogui.hotkey('ctrl', 'alt') # Пример сочетания клавиш Ctrl+Alt+Shift+B

    # Скриншот экрана
    screen = pyautogui.screenshot(region=(0, 0, pyautogui.size().width, pyautogui.size().height))
    screen = np.array(screen)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

    # Поиск совпадений
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # Отображение прямоугольников вокруг совпадений и вывод координат
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        print(f'Совпадение найдено в точке {pt[0]}, {pt[1]}')

    # Отображение изображения с прямоугольниками
    cv2.imshow('Matched', screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    keyboard.wait('u')
    break

