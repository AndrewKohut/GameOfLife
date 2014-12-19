__author__ = 'cleoh_000'
import tkinter
import random

class Drawer:
    size = 0
    root = 0
    canv = 0
    grid_step = 0
    arr_size = 0
    population = []
    speed = 0

    def __init__(self, size, grid, speed):
        self.size = size
        self.grid_step = grid
        self.speed = speed
        self.population = self.create_population()
        self.root = tkinter.Tk()
        self.root.title = "Conway's Game of Life"
        self.canv = tkinter.Canvas(self.root, width=size, height=size, bg="white")
        self.canv.pack()
        self.start_game()
        self.root.mainloop()

    def draw_grid(self, step):
        self.grid_step = step
        for i in range(self.size//step):
            self.canv.create_line(i*step, 0, i*step, self.size, fill="#D8D8D8 ")
            self.canv.create_line(0, i*step, self.size, i*step, fill="#D8D8D8 ")

    def create_population(self):
        count = self.size // self.grid_step
        self.arr_size = count
        return [[random.randint(0, 1) for x in range(self.arr_size)] for r in range(self.arr_size)]

    def try_get_item(self, a, i, j):
        print(i, j)
        if i < 0 or j < 0:
            return 0
        if i >= len(a) or j >= len(a):
            return 0

        return a[i][j]

    def check_population(self, a):
        new = [[0 for x in range(self.arr_size)] for r in range(self.arr_size)]
        for i in range(self.arr_size):
            for j in range(self.arr_size):
                new[i][j] = self.get_state(a, i, j)
        return new

    def start_game(self):
        self.draw_grid(self.grid_step)
        self.draw(self.population)
        while True:
            new = self.check_population(self.population)
            self.draw(new)
            self.population = new
            self.canv.update()
            self.canv.after(self.speed)

    def draw(self, a):
        for i in range(self.arr_size):
            for j in range(self.arr_size):
                if self.population[i][j] != a[i][j]:
                    if a[i][j] == 1:
                        self.draw_oval(i, j, True)
                    else:
                        self.canv.delete("{0}:{1}".format(i,j))

    def draw_oval(self, i, j, b):
            x = i * self.grid_step
            y = j * self.grid_step
            size = (self.grid_step - 1) // 2
            self.canv.create_oval(x + size // 2, y + size // 2, x + size * 2, y + size * 2, outline="black" if b else "white", tag="{0}:{1}".format(i, j))

    def can_up(self, i):
        return True if i > 0 else False

    def can_down(self, i):
        return True if i < self.arr_size - 1 else False

    def can_left(self, j):
        return True if j > 0 else False

    def can_right(self, j):
        return True if j < self.arr_size - 1 else False

    def get_state(self, a, i, j):
        count = 0
        # count += self.try_get_item(a, i - 1, j)
        # count += self.try_get_item(a, i + 1, j)
        # count += self.try_get_item(a, i, j - 1)
        # count += self.try_get_item(a, i, j + 1)
        # count += self.try_get_item(a, i - 1, j - 1)
        # count += self.try_get_item(a, i - 1, j + 1)
        # count += self.try_get_item(a, i + 1, j - 1)
        # count += self.try_get_item(a, i + 1, j + 1)

        if self.can_up(i):
            if a[i - 1][j] == 1:
                count += 1
        if self.can_down(i):
            if a[i + 1][j] == 1:
                count += 1
        if self.can_left(j):
            if a[i][j - 1] == 1:
                count += 1
        if self.can_right(j):
            if a[i][j + 1] == 1:
                count += 1

        if self.can_up(i) and self.can_left(j):
            if a[i - 1][j - 1] == 1:
                count += 1
        if self.can_up(i) and self.can_right(j):
            if a[i - 1][j + 1] == 1:
                count += 1
        if self.can_down(i) and self.can_left(j):
            if a[i + 1][j - 1] == 1:
                count += 1
        if self.can_down(i) and self.can_right(j):
            if a[i + 1][j + 1] == 1:
                count += 1

        if a[i][j] == 1:
            if count == 2 or count == 3:
                return a[i][j]
            else:
                return 0
        elif count == 3:
            return 1
