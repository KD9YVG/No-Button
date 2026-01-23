import tkinter as tk
import random

database = "database.txt"
dataList = []

print("Loading database...")
with open(database, 'r') as file:
    for line in file:
        dataList.append(line.strip())
print(f"Loaded {len(dataList)} entries from the database.")

root = tk.Tk()
root.title("No Button")
root.geometry("300x300")

def generateNo():
    index = random.randint(0, len(dataList) - 1)
    return str(dataList[index])[1:-2]

def updateScreen():
    generateNo()
    textArea.config(state=tk.NORMAL)
    textArea.delete("1.0", tk.END)
    textArea.insert(tk.END, generateNo())
    textArea.config(state=tk.DISABLED)

## Elements
textArea = tk.Text(width=40, height=10, state="disabled", wrap="word")
noButton = tk.Button(text="No", command=updateScreen)

## Place elements
textArea.pack(padx=10,pady=10)
noButton.pack(padx=5, pady=5)

## Main Loop
tk.mainloop()