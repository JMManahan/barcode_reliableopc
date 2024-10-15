import sqlite3
import tkinter as tk
from tkinter import messagebox

def lookup_barcode(barcode):
    # Connect to the SQLite database
    conn = sqlite3.connect('barcode_data.db')
    c = conn.cursor()

    # Query the database for the barcode
    c.execute("SELECT * FROM barcodes WHERE id=?", (barcode,))
    result = c.fetchone()

    # Close the connection
    conn.close()

    # Display the result
    if result:
        output = f"ID: {result[0]}\nName: {result[1]}\nDepartment: {result[2]}\nPosition: {result[3]}"
        messagebox.showinfo("Barcode Information", output)
    else:
        messagebox.showwarning("Not Found", "No information found.")

def on_scan_button_click():
    scanned_barcode = entry.get()  # Get the input from the entry field
    if scanned_barcode:
        lookup_barcode(scanned_barcode)
    else:
        messagebox.showwarning("Input Error", "Please enter a barcode ID.")

def on_enter_pressed(event):
    # Call the scan function when Enter is pressed
    on_scan_button_click()

# Create the main window
root = tk.Tk()
root.title("Barcode Scanner")
root.geometry("300x200")  # Set window size

# Create a label
label = tk.Label(root, text="Scan a barcode ID:")
label.pack(pady=10)  # Add some vertical padding

# Create an entry field for barcode input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Bind the Enter key to trigger the scanning function
entry.bind('<Return>', on_enter_pressed)

# Create a scan button
scan_button = tk.Button(root, text="Scan Barcode", command=on_scan_button_click)
scan_button.pack(pady=20)

# Automatically focus on the entry field
entry.focus_set()

# Start the GUI event loop
root.mainloop()