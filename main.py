import tkinter as tk
from tkinter import ttk
import random
import pyttsx3
import threading

database = "database.txt"
dataList = []

print("Loading database...")
with open(database, 'r', encoding='utf-8') as file:
    for line in file:
        dataList.append(line.strip())
print(f"Loaded {len(dataList)} entries from the database.")

root = tk.Tk()
root.title("No Button")
root.geometry("300x300")

## Generate No message returned as string
def generateNo():
    index = random.randint(0, len(dataList) - 1)
    return str(dataList[index])

## Calls generateNo() and sets the GUI to show the no message
def updateScreen():
    generateNo()
    textArea.config(state=tk.NORMAL)
    textArea.delete("1.0", tk.END)
    textArea.insert(tk.END, generateNo())
    textArea.config(state=tk.DISABLED)

## speak_task() is a thread that takes the GUI text and speaks it. speak() is the function to start this thread
def speak_task():
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.stop()
        engine.say(textArea.get("1.0", tk.END))
        engine.runAndWait()
    except Exception as e:
        print(f"Speech Error: {e}")
def speak():
    threading.Thread(target=speak_task, daemon=True).start()

## GUI Elements
textArea = tk.Text(width=40, height=10, state="disabled", wrap="word")
noButton = tk.Button(text="No", command=updateScreen)
speakButton = tk.Button(text="Speak", command=speak)

## Place elements
textArea.pack(padx=10,pady=10)
noButton.pack(padx=5, pady=5)
speakButton.pack(padx=5, pady=5)

# Main Loop
try:
    tk.mainloop()
except KeyboardInterrupt:
    print("Exiting from keyboad interrupt.")
    exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)