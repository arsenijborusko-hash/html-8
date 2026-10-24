import time
import turtle
import random

WIDTH=500
HEIGHT=500
COLORS=["green", "blue", "red", "black", "orange", "yellow", "pink", "purple", "blue", "brown"]


def get_number_of_racers():
    while True:
        racers = input("Введите количество черепах для гонки от 2 до 10: ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Вы ввели не число, попробуйте ещё раз: ")
            continue
        if  2 <= racers <= 10:
            return racers
        else:
            print("Введите количество черепах от 2 до 10:")
        

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Черепашьи бега")
    time.sleep(5)


def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for index, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.left(90)
        t.penup()
        t.shape("turtle")
        t.setpos(-WIDTH //2 + (index + 1) * spacing, -HEIGHT//2 + 20 )
        t.pendown()
        turtles.append(t)
    return turtles


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def main():
    random.shuffle(COLORS)
    colors = COLORS[:get_number_of_racers()]
    init_turtle()
    print(f"Победила черепаха {race(colors)} цвета")


if __name__ == '__main__':
   main()