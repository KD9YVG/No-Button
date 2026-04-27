import tkinter as tk
import random
import pyttsx3
import threading
import filter

# Using functions from filter.py in the same directory, we import all strings listed in the 
# database file that are not listed in the blocked file. We then display the number blocked and
# imported to the user in the terminal
print("Loading database...")
filtered = filter.importData(filter=True, debug=True)
dataList = filtered["data"]
print(f"Loaded {len(dataList)} entries from {filtered["dataPath"]}. Blocked {filtered["amountBlocked"]} from {filtered["blockedPath"]}.")

# Creates a graphical window
root = tk.Tk()
root.title("No Button")
root.geometry("300x300")

def generateNo():
    """
    This function generates a random number and uses that to pick a 
    random no message. It then returns that no message as a string. 
    """
    index = random.randint(0, len(dataList) - 1)
    return dataList[index]

def updateScreen():
    """
    This function clears the textArea and calls generateNo() to 
    update the textArea with a new no message. 
    """
    textArea.config(state=tk.NORMAL)
    textArea.delete("1.0", tk.END)
    textArea.insert(tk.END, generateNo())
    textArea.config(state=tk.DISABLED)

def speak_task(text):
    """
    Using the pyttsx3 library, we create a new engine, set the speach
    rate, stop any existing text, que the parameter to be spoken and 
    then speak the text. Because runAndWait() locks the thread until
    the engine is finished speaking, this function should only be used
    with threading. 
    :param text: 
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech Error: {e}")
def speak():
    """
    Because tkinter only can run one command on a button press, this
    function gets the text from the textArea and ques it to be spoken
    using the speak_task function.
    """
    words = textArea.get("1.0", tk.END).strip()
    threading.Thread(target=speak_task, args=(words,), daemon=True).start()

# We create the three elements used in our GUI and set their atributes. When the
# user presses the "No" button, it updates the screen. When the user presses the
# "Speak" button, we call the speak function to start the speaking process.
textArea = tk.Text(width=40, height=10, state="disabled", wrap="word")
noButton = tk.Button(text="No", command=updateScreen)
speakButton = tk.Button(text="Speak", command=speak)

# We then pack (place) the elements on the screen with padding
textArea.pack(padx=10,pady=10)
noButton.pack(padx=5, pady=5)
speakButton.pack(padx=5, pady=5)

# We update the screen before showing the window so there is a message waiting for
# the user when the first open the app, then start the tkinter mainloop. This lets us
# wait for user input from the GUI and call our functions appropriatly.
try:
    updateScreen()
    tk.mainloop()
except KeyboardInterrupt:
    print("Exiting from keyboard interrupt.")
    exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)
