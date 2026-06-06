import tkinter as tk
from tkinter import messagebox
INCH_TO_CM = 2.54

def convert_to_cm():
    """Convert inches to centimeters and display the result."""
    try:
        inches = float(entry_inches.get())
        cm = inches * INCH_TO_CM
        result_var.set(f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        result_var.set("")
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")
root.resizable(False, False)
tk.Label(root, text="Inches to Centimeters Converter", font=("Arial", 14, "bold")).pack(pady=10)
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Enter length in inches:").grid(row=0, column=0, padx=5, pady=5)
entry_inches = tk.Entry(frame_input, width=15)
entry_inches.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=convert_to_cm, width=15, bg="blue", fg="white").pack(pady=10)
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), fg="green").pack(pady=5)
root.mainloop()
