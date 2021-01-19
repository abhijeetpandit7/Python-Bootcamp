# Colorgram lets extract color from images
import colorgram
import turtle
import random

turtle.colormode(255)

# Extract 30 colors from image.jpg
# Returns 30 color object containing rgb & hsl value
colors = colorgram.extract('image.jpg',30)
rgb_colors = []
for color in colors:
    rgb = color.rgb
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

# Slimming rgb_colors to remove unwanted tuple
color_list = [ 
    (111, 145, 98), (190, 154,125), (137, 84, 66), (22, 26, 48), (143, 158, 186), 
    (228, 223, 111), (80, 91, 124), (134, 71, 88), (185, 143, 157), (50, 31, 22), 
    (61, 25, 35), (150, 174, 160), (26, 36, 28), (115, 36, 49), (82, 100, 87), 
    (46, 50, 107), (173, 99, 124), (118, 40, 34), (173, 182, 223), (186, 99, 85), 
    (104, 114, 178), (226, 177, 169), (221, 174, 186), (68, 73, 44), (172, 200, 204), 
    (172, 202, 189)
]

tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
for y in range(0,500,50):
    tim.sety(y-250)
    for x in range(0,500,50):
        tim.setx(x-250)
        tim.dot(20, random.choice(color_list))
        
screen = turtle.Screen()
screen.exitonclick()