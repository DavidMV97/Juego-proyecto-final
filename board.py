import tkinter as tk
import math

def draw_divided_circle(canvas, x, y, radius, data):
    # Dibujar el círculo
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", width=2)

    # Calcular los ángulos de las divisiones
    angles = [i * (2 * math.pi) / 5 for i in range(5)]

    # Dibujar las divisiones coloreadas
    colors = ["red", "green", "blue", "yellow", "orange"]
    for i, angle in enumerate(angles):
        # x1 = x + radius * math.cos(angle)
        # y1 = y - radius * math.sin(angle)
        # x2 = x + radius * math.cos(angles[(i + 1) % 5])
        # y2 = y - radius * math.sin(angles[(i + 1) % 5])
        canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=math.degrees(angle), extent=360/5, style=tk.PIESLICE, outline="", fill=colors[i])

        # Calcular el número de elementos en esta parte del círculo grande
        num_elements = len(data[i])

        # Dibujar los elementos
        element_radius = -10
        for j in range(num_elements):
            element_angle = angle + (j * math.pi / (10 * (i + 1)))  # Ajustar el ángulo para cada elemento
            element_x = x + (radius + element_radius) * math.cos(element_angle)
            element_y = y - (radius + element_radius) * math.sin(element_angle)
            canvas.create_text(element_x, element_y, text=data[i][j], fill="white")


