import tkinter as tk
import random
import pyttsx3
import threading
import filter

print("Loading database...")
filtered = filter.importData()
dataList = filtered["data"]
print(f"Loaded {len(dataList)} entries from {filtered["dataPath"]}. Blocked {filtered["amountBlocked"]} from {filtered["blockedPath"]}.")

root = tk.Tk()
root.title("No Button")
root.geometry("300x300")

def generateNo():
    index = random.randint(0, len(dataList) - 1)
    return str(dataList[index])

def updateScreen():
    generateNo()
    textArea.config(state=tk.NORMAL)
    textArea.delete("1.0", tk.END)
    textArea.insert(tk.END, generateNo())
    textArea.config(state=tk.DISABLED)


def speak_task(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech Error: {e}")
def speak():
    words = textArea.get("1.0", tk.END)
    threading.Thread(target=speak_task(words), daemon=True).start()

## Elements
textArea = tk.Text(width=40, height=10, state="disabled", wrap="word")
noButton = tk.Button(text="No", command=updateScreen)
speakButton = tk.Button(text="Speak", command=speak)

## Place elements
textArea.pack(padx=10,pady=10)
noButton.pack(padx=5, pady=5)
speakButton.pack(padx=5, pady=5)

# Main Loop
try:
    updateScreen()
    tk.mainloop()

except KeyboardInterrupt:
    print("Exiting from keyboad interrupt.")
    exit(0)

except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)