import tkinter as tk
from tkinter import filedialog
import pandas as pd

def compare_xml_files(file1, file2):
    # Read the first XML file into Pandas
    df1 = pd.read_xml(file1)

    # Read the second XML file into Pandas
    df2 = pd.read_xml(file2)

    # Find the common columns between the two xml's
    common_columns = list(set(df1.columns) & set(df2.columns))

    # Filter the first xml to only include the common columns
    df1 = df1[common_columns]

    # Filter the second xml to only include the common columns
    df2 = df2[common_columns]

    # combine the two xmls on the common columns
    merged_df = pd.merge(df1, df2, on=common_columns, how='inner')

    # Write the combined xml's to a new xml file
    merged_df.to_xml('merged_data.xml', index=False)
    status_label.config(text="Output file generated successfully.")

def browse_file():
    file_path = filedialog.askopenfilename()
    return file_path

def run_comparison():
    file1 = file1_path.get()
    file2 = file2_path.get()
    compare_xml_files(file1, file2)

# Cmain tk window
root = tk.Tk()
root.title("XML File Comparator")
root.geometry("600x300")
root.config(bg="gray10")

# file input and browse
file1_label = tk.Label(root, text="Select File 1", fg="white", bg="gray10", font=("Arial", 12))
file1_label.grid(row=0, column=0, padx=10, pady=10)
file1_path = tk.StringVar()
file1_path.set("")
file1_entry = tk.Entry(root, textvariable=file1_path, width=50)
file1_entry.grid(row=0, column=1, padx=10, pady=10)
file1_button = tk.Button(root, text="Browse", command=lambda: file1_path.set(browse_file()), bg="gray")
file1_button.grid(row=0, column=2, padx=10, pady=10)

file2_label = tk.Label(root, text="Select File 2", fg="white", bg="gray10", font=("Arial", 12))
file2_label.grid(row=1, column=0, padx=10, pady=10)
file2_path = tk.StringVar()
file2_path.set("")
file2_entry = tk.Entry(root, textvariable=file2_path, width=50)
file2_entry.grid(row=1, column=1, padx=10, pady=10)
file2_button = tk.Button(root, text="Browse", command=lambda: file2_path.set(browse_file()), bg="gray")
file2_button.grid(row=1, column=2, padx=10, pady=10)

# run button
run_button = tk.Button(root, text="Run Comparison", command=run_comparison, bg="gray")
run_button.grid(row=2, column=1, padx=10, pady=10)

# status label
status_label = tk.Label(root, text="", fg="white", bg="gray10", font=("Arial", 12))
status_label.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
