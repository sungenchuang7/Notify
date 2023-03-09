import PySimpleGUI as sg
import subprocess

# define the PySimpleGUI layout
layout = [
    [sg.Text("Press the button to start recording")],
    [sg.Button("Start Recording"), sg.Button("Stop Recording")]
]

# create the PySimpleGUI window
window = sg.Window("Notify", layout)

# variable to store the Popen object
p = None

# event loop to process PySimpleGUI events
while True:
    event, values = window.read()
    if event == "Stop Recording":
        # terminate the process if it is running
        if p is not None:
            p.terminate()
        break
    elif event == "Start Recording":
        # start the process using Popen
        p = subprocess.Popen(["python3", "backend.py"])

# close the PySimpleGUI window
window.close()
