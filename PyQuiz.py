import tkinter as tk
from tkinter import messagebox
import io
import sys

# ----------------------------
# Data: Coding Challenges
# ----------------------------
challenges = [
    {
        "task": "Print 'Hello World!'",
        "expected_output": "Hello World!",
        "explanation": "The print function outputs text to the console. In simple terms, it displays whatever is in the parentheses."
    },
    {
        "task": "Print the sum of 5 and 7",
        "expected_output": "12",
        "explanation": "+ operator is used for addition and joining (concatenation).\nFor numbers: it adds them.\nprint(5+7)\nOutput: 12\nFor strings: it joins them together.\nprint('Hello' + 'World')\nOutput: Hello World"
    },
    {
        "task": "Check if a in List [1,2,3,4]",
        "expected_output": "True",
        "explanation": "In Python, 'in' is called a membership operator. It checks whether a value exists inside a sequence (like a list, string, or tuple). It returns True if the value is found, otherwise False."
    },
    {
        "task": "Print numbers from 1 to 3 (each on new line)",
        "expected_output": "1\n2\n3",
        "explanation": "1st method: Using multiple print statements.\nprint(1)\nprint(2)\nprint(3)\nPreferred when you have a small number of values to print.\n2nd method: Use a loop to iterate the numbers and print each one.\nfor i in range(1,4):\n\tprint(i)"
    }
]

# ----------------------------
# Game Variables
# ----------------------------
score = 0
lives = 3
level = 0

# ----------------------------
# Functions
# ----------------------------
def run_code():
    global score, lives, level
    user_code = code_input.get("1.0", tk.END)

    # Capture printed output
    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        exec(user_code)
    except Exception as e:
        sys.stdout = sys.__stdout__
        messagebox.showerror("Error", f"⚠️ Error in your code:\n{e}")
        lives -= 1
        update_status()
        if lives == 0:
            game_over()
        return
    
    sys.stdout = sys.__stdout__
    output = buffer.getvalue().strip()  # remove extra newlines/spaces
    expected = str(challenges[level]["expected_output"]).strip()

    if output == expected:
        messagebox.showinfo(
            "Success", 
            f"✅ Correct output! Moving to next level.\n\nExplanation:\n{challenges[level]['explanation']}"
        )
        score += 10
        level += 1
        if level < len(challenges):
            load_next_challenge()
        else:
            win_game()
    else:
        lives -= 1
        messagebox.showerror(
            "Incorrect",
            f"❌ Wrong output!\n\nExpected:\n{expected}\n\nYour Output:\n{output}"
        )
        update_status()
        if lives == 0:
            game_over()

def load_next_challenge():
    code_input.delete("1.0", tk.END)
    task_label.config(text=f"Task: {challenges[level]['task']}")
    update_status()

def update_status():
    status_label.config(text=f"Score: {score} | Lives: {lives} | Level: {level + 1}")

def game_over():
    messagebox.showinfo("Game Over", f"💀 Game Over!\nFinal Score: {score}")
    window.destroy()

def win_game():
    messagebox.showinfo("Victory", f"🎉 Congratulations!\nYou completed all levels!\nFinal Score: {score}")
    window.destroy()

# ----------------------------
# Tkinter GUI Setup (Beautified)
# ----------------------------
window = tk.Tk()
window.title("🐍 Python Quiz")
window.geometry("700x550")
window.config(bg="#1a1a1a")  # Dark background

# Title Label
title_label = tk.Label(window, text="🐍 Python Quiz", fg="#00ff7f", bg="#1a1a1a", font=("Consolas", 28, "bold"))
title_label.pack(pady=20)

# Task Label Frame
task_frame = tk.Frame(window, bg="#282828", padx=20, pady=10)
task_frame.pack(pady=10, fill="x", padx=50)

task_label = tk.Label(task_frame, text=f"Task: {challenges[level]['task']}", fg="#ffffff", bg="#282828", font=("Consolas", 14))
task_label.pack()

# Code Input Box
code_input = tk.Text(window, height=12, width=80, bg="#2b2b2b", fg="white", insertbackground="white", font=("Consolas", 12), bd=0, highlightthickness=2, highlightbackground="#00ff7f")
code_input.pack(pady=15)

# Run Button with Hover Effect
def on_enter(e):
    run_button['bg'] = "#00cc66"
def on_leave(e):
    run_button['bg'] = "#00ff7f"

run_button = tk.Button(window, text="▶ Run Code", command=run_code, font=("Consolas", 14, "bold"), bg="#00ff7f", fg="#1a1a1a", width=18, bd=0, activebackground="#00cc66", activeforeground="white")
run_button.pack(pady=10)
run_button.bind("<Enter>", on_enter)
run_button.bind("<Leave>", on_leave)

# Status Label
status_label = tk.Label(window, text=f"Score: {score} | Lives: {lives} | Level: {level + 1}", fg="white", bg="#282828", font=("Consolas", 12), padx=10, pady=5)
status_label.pack(pady=15)

# Start GUI
window.mainloop()
