import tkinter as tk
from tkinter import messagebox
import re
import hashlib

# Create the main application window
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x350")  # Set window size

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one uppercase letter.\n"

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one lowercase letter.\n"

    # Check digit
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "Password should contain at least one number.\n"

    # Check special character
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one special character (@, $, etc.).\n"

    # Determine strength level
    if strength == 5:
        return "Strong", "Your password is strong!"
    elif strength >= 3:
        return "Moderate", "Consider adding more complexity."
    else:
        return "Weak", remarks

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed
def analyze_password():
    password = password_entry.get()  # Get password input
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    strength, feedback = check_password_strength(password)
    hashed_pass = hash_password(password)  # Encrypt password

    result_label.config(text=f"Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")
    feedback_label.config(text=feedback)
    hash_label.config(text=f"Hashed Password (SHA-256):\n{hashed_pass[:30]}...")  # Show part of hash

# GUI Components
password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Password", command=analyze_password)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

feedback_label = tk.Label(root, text="", wraplength=350, justify="left")
feedback_label.pack()

hash_label = tk.Label(root, text="", wraplength=350, justify="left", fg="blue")
hash_label.pack()

# Run the application
root.mainloop()
