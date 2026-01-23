import random
import tkinter as tk
from tkinter import ttk
import pyttsx3
import threading


database = 'database.txt'
dataList = []

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine_lock = threading.Lock()

print("Loading database...")
with open(database, 'r') as file:
    for line in file:
        dataList.append(line.strip())
print(f"Loaded {len(dataList)} entries from the database.")

def randomNo():
    index = random.randint(0, len(dataList) - 1)
    output = dataList[index]
    return output

def speak_task():
    """
    Uses a threading Lock to ensure only one speech command 
    is sent to the system at a time.
    """
    # The 'with' statement ensures the lock is released even if an error occurs
    with engine_lock:
        try:
            engine.say("No")
            engine.runAndWait()
        except Exception as e:
            print(f"Speech Error: {e}")

def speak():
    threading.Thread(target=speak_task, daemon=True).start()

def onNoClick():
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, randomNo())

## GUI Creation
root = tk.Tk()
root.title("No Button")
root.geometry("300x300")

output_area = tk.Text(root, height=10, width=30)
no_button = tk.Button(root, text="No", command=onNoClick, foreground="red", width=15)
speak_button = tk.Button(root, text="Speak", command=speak, foreground="blue", width=15)
bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate', value=50)

output_area.pack(pady=10, padx=10)
no_button.pack(pady=5)
speak_button.pack(pady=5)
bar.pack(pady=10)


## Main
root.mainloop()