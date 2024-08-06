import turtle
import tkinter as tk
from tkinter import colorchooser, filedialog
import json

# Initialize the main window
root = tk.Tk()
root.title("Turtle Graphics App")

# Initialize the turtle screen and canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(side=tk.TOP)
screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(-300, -200, 300, 200)

# Create a turtle
t = turtle.RawTurtle(screen)
t.speed(1)

# Record movements
movements = []

def record_movement(heading, distance, color):
    """
    Record each movement of the turtle with its heading, distance, and color.
    
    Args:
    heading (int): The heading direction of the turtle.
    distance (int): The distance the turtle moved.
    color (str): The color of the turtle during the movement.
    """
    movements.append({"heading": heading, "distance": distance, "color": color})

# Function to move the turtle up
def move_up():
    """
    Move the turtle up by the distance specified in the entry field.
    """
    distance = entry_up.get()
    if distance.isdigit():
        t.setheading(90)
        t.forward(int(distance))
        record_movement(90, int(distance), t.color()[0])

# Function to move the turtle down
def move_down():
    """
    Move the turtle down by the distance specified in the entry field.
    """
    distance = entry_down.get()
    if distance.isdigit():
        t.setheading(270)
        t.forward(int(distance))
        record_movement(270, int(distance), t.color()[0])

# Function to move the turtle right
def move_right():
    """
    Move the turtle right by the distance specified in the entry field.
    """
    distance = entry_right.get()
    if distance.isdigit():
        t.setheading(0)
        t.forward(int(distance))
        record_movement(0, int(distance), t.color()[0])

# Function to move the turtle left
def move_left():
    """
    Move the turtle left by the distance specified in the entry field.
    """
    distance = entry_left.get()
    if distance.isdigit():
        t.setheading(180)
        t.forward(int(distance))
        record_movement(180, int(distance), t.color()[0])

# Function to change turtle color
def change_color():
    """
    Open a color chooser to change the turtle's color.
    """
    color = colorchooser.askcolor()[1]
    if color:
        t.color(color)

# Function to reset turtle position
def reset_position():
    """
    Reset the turtle's position to the center of the screen.
    """
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Function to clear the canvas
def clear_canvas():
    """
    Clear the canvas and reset the turtle's state.
    """
    screen.clearscreen()
    screen.setworldcoordinates(-300, -200, 300, 200)
    global t
    t = turtle.RawTurtle(screen)
    t.speed(1)
    movements.clear()

# Function to save drawing
def save_drawing():
    """
    Save the current drawing to a JSON file.
    """
    drawing_data = {"movements": movements, "color": t.color()[0]}
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(drawing_data, file)

# Function to load drawing
def load_drawing():
    """
    Load a drawing from a JSON file and replay the movements.
    """
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            drawing_data = json.load(file)
            movements.clear()
            t.reset()
            for movement in drawing_data["movements"]:
                t.color(movement["color"])
                t.setheading(movement["heading"])
                t.forward(movement["distance"])
                movements.append(movement)

# Create the control panel with buttons and entry fields
control_panel = tk.Frame(root)
control_panel.pack(side=tk.BOTTOM)

# Up movement control
tk.Label(control_panel, text="Go Up").grid(row=0, column=0)
entry_up = tk.Entry(control_panel)
entry_up.grid(row=0, column=1)
tk.Button(control_panel, text="Move Up", command=move_up).grid(row=0, column=2)

# Down movement control
tk.Label(control_panel, text="Go Down").grid(row=1, column=0)
entry_down = tk.Entry(control_panel)
entry_down.grid(row=1, column=1)
tk.Button(control_panel, text="Move Down", command=move_down).grid(row=1, column=2)

# Right movement control
tk.Label(control_panel, text="Go Right").grid(row=2, column=0)
entry_right = tk.Entry(control_panel)
entry_right.grid(row=2, column=1)
tk.Button(control_panel, text="Move Right", command=move_right).grid(row=2, column=2)

# Left movement control
tk.Label(control_panel, text="Go Left").grid(row=3, column=0)
entry_left = tk.Entry(control_panel)
entry_left.grid(row=3, column=1)
tk.Button(control_panel, text="Move Left", command=move_left).grid(row=3, column=2)

# Color change control
tk.Button(control_panel, text="Change Color", command=change_color).grid(row=4, column=0)

# Reset position control
tk.Button(control_panel, text="Reset Position", command=reset_position).grid(row=4, column=1)

# Clear canvas control
tk.Button(control_panel, text="Clear Canvas", command=clear_canvas).grid(row=4, column=2)

# Save drawing control
tk.Button(control_panel, text="Save Drawing", command=save_drawing).grid(row=5, column=0)

# Load drawing control
tk.Button(control_panel, text="Load Drawing", command=load_drawing).grid(row=5, column=1)

# Main loop to run the application
root.mainloop()
