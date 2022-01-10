

import pygame as pg
import copy
import menu
import sys

# размеры игрового поля и клетки
WIDTH, HEIGHT = 1000, 500
cellsize = 10

# подсчёт кол-ва клеток по осям
cells_w_cnt = WIDTH // cellsize
cells_h_cnt = HEIGHT // cellsize


# списки клеток на нынешнем и следующем шаге
cells_now = [[0 for _ in range(cells_w_cnt)] for _ in range(cells_h_cnt)]
cells_next = [[0 for _ in range(cells_w_cnt)] for _ in range(cells_h_cnt)]


def is_alive(pos: tuple, status: int) -> int:
    """проверка соседей и вычисление сосотяния клетки"""

    p = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    count = 0
    for y, x in p:
        i, j = pos[0] + y, pos[1] + x
        if 0 <= j < cells_w_cnt and 0 <= i < cells_h_cnt and cells_now[i][j] == 1:
            count += 1

    if status == 0 and count == 3:
        return 1
    if status == 1 and 2 <= count <= 3:
        return 1
    return 0


def drawing_background():
    """заполнение фона и отрисовка сетки"""

    surface.fill(pg.Color("black"))
    for i in range(cells_w_cnt):
        pg.draw.line(surface, (10, 10, 10), (i * cellsize, 0), (i * cellsize, WIDTH))
    for i in range(cells_h_cnt):
        pg.draw.line(surface, (10, 10, 10), (0, i * cellsize), (WIDTH, i * cellsize))


def drawing_cells():
    """подсчёт состояния игры на следующем шаге и его отрисовка"""

    for i in range(cells_h_cnt):
        for j in range(cells_w_cnt):
            status = cells_now[i][j]
            if cells_now[i][j] == 1:
                pg.draw.rect(
                    surface,
                    pg.Color("forestgreen"),
                    (j * cellsize, i * cellsize, cellsize, cellsize),
                )
            cells_next[i][j] = is_alive((i, j), status)


def drawing_on_start():
    """прорисовка начального вида игры пользователем"""

    for i in range(cells_h_cnt):
        for j in range(cells_w_cnt):
            if cells_now[i][j] == 1:
                pg.draw.rect(
                    surface,
                    pg.Color("forestgreen"),
                    (j * cellsize, i * cellsize, cellsize, cellsize),
                )


def drawing_main(fps=10):
    """вывод текущего состояния игры на экран"""
    drawing_background()
    drawing_cells()
    pg.display.flip()
    clock.tick(fps)


# вызов окна меню
app = menu.QtWidgets.QApplication(sys.argv)
Dialog = menu.QtWidgets.QDialog()
ui = menu.Ui_Dialog()
ui.setupUi(Dialog, True)
Dialog.show()
app.exec_()

# инициализация игры
pg.init()
surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("GameOfLife")
clock = pg.time.Clock()

beginning = True
while beginning:
    # цикл для создания начальных услових игры
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN and event.key in (pg.K_RETURN, pg.K_SPACE):
            beginning = False

    # установка клеток по кликам мышки
    pressed_mouse = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    x, y = pos[0] // cellsize, pos[1] // cellsize
    if pressed_mouse[0]:
        cells_now[y][x] = 1
        drawing_on_start()
    elif pressed_mouse[2]:
        cells_now[y][x] = 0
        drawing_on_start()
    drawing_main(fps=120)

paused = False
while True:
    # цикл, запускающий процесс игры
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            paused = not paused
    if not paused:
        drawing_main(fps=10)
        cells_now = copy.deepcopy(cells_next)
