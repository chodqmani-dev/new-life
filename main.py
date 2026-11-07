
import turtle
import math
import pygame
import os

# -------------------------------
# 1. LOAD BACKGROUND MUSIC
# -------------------------------

folder = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(folder, "music.mp3")

pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(-1)

# -------------------------------
# 2. CREATE TURTLE SCREEN
# -------------------------------

screen = turtle.Screen()
screen.setup(850, 800)
screen.bgcolor("black")
screen.title("INFINITE LOVE YOU")
screen.tracer(0)

# -------------------------------
# 3. CREATE HEART POINTS
# -------------------------------

points = []

for i in range(120):
    t = 2 * math.pi * i / 120

    x = 16 * math.sin(t)**3

    y = (
        13 * math.cos(t)
        - 5 * math.cos(2*t)
        - 2 * math.cos(3*t)
        - math.cos(4*t)
    )

    points.append((x * 15, y * 15))

# -------------------------------
# 4. LOVE YOU ANIMATION
# -------------------------------


# -------------------------------
# 4. LOVE YOU INFINITE ANIMATION
# -------------------------------


# -------------------------------
# 4. INFINITE LAYER-BY-LAYER HEART
# -------------------------------

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

index = 0
layer = 0

message = " I LOVE YOU NANNA ♥"

def animate():
    global index, layer

    # Increase the heart size after each completed layer
    scale = 15 + (layer * 2)

    t = 2 * math.pi * index / len(points)

    x = 16 * math.sin(t)**3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2*t)
        - 2 * math.cos(3*t)
        - math.cos(4*t)
    )

    pen.goto(x * scale, y * scale)
    pen.color("#ffa8d3")

    pen.write(
        message,
        align="center",
        font=("Arial", 11, "bold")
    )

    index += 1

    # Finish current layer and start the next larger layer
    if index >= len(points):
        index = 0
        layer += 1

    screen.update()
    screen.ontimer(animate, 35)

# -------------------------------
# 5. START INFINITE ANIMATION
# -------------------------------

animate()
turtle.done()
