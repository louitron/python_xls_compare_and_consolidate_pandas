import tkinter as tk
from tkinter import filedialog
import pandas as pd

def compare_excel_files(file1, file2):
    # Read the first Excel file into a Pandas dataframe
    df1 = pd.read_excel(file1)

    # Read the second Excel file into a Pandas dataframe
    df2 = pd.read_excel(file2)

    # Find the common columns between the two dataframes
    common_columns = list(set(df1.columns) & set(df2.columns))

    # Filter the first excel to only include the common columns
    df1 = df1[common_columns]

    # Filter the second excel to only include the common columns
    df2 = df2[common_columns]

    # Merge the two excel on the common columns
    merged_df = pd.merge(df1, df2, on=common_columns, how='inner')

    # Write the merged excel to a new Excel file
    merged_df.to_excel('merged_data.xlsx', index=False)
    status_label.config(text="Comparison and new file generated successfully.")

def browse_file():
    file_path = filedialog.askopenfilename()
    return file_path

def run_comparison():
    file1 = file1_path.get()
    file2 = file2_path.get()
    compare_excel_files(file1, file2)

# Create the main window
root = tk.Tk()
root.title("Excel File Comparison")
root.geometry("600x300")
root.config(bg="gray10")

# Create the file input fields and browse buttons
file1_label = tk.Label(root, text="Select Workbook 1", fg="white", bg="gray10", font=("Arial", 12))
file1_label.grid(row=0, column=0, padx=10, pady=10)
file1_path = tk.StringVar()
file1_path.set("")
file1_entry = tk.Entry(root, textvariable=file1_path, width=50)
file1_entry.grid(row=0, column=1, padx=10, pady=10)
file1_button = tk.Button(root, text="Browse", command=lambda: file1_path.set(browse_file()), bg="olive")
file1_button.grid(row=0, column=2, padx=10, pady=40)

file2_label = tk.Label(root, text="SelectWorkbook 2", fg="white", bg="gray10", font=("Arial", 12))
file2_label.grid(row=1, column=0, padx=30, pady=10)
file2_path = tk.StringVar()
file2_path.set("")
file2_entry = tk.Entry(root, textvariable=file2_path, width=50)
file2_entry.grid(row=1, column=1, padx=10, pady=10)
file2_button = tk.Button(root, text="Browse", command=lambda: file2_path.set(browse_file()), bg="olive")
file2_button.grid(row=1, column=2, padx=10, pady=10)

# Create the run button
run_button = tk.Button(root, text="Run Comparison", command=run_comparison, bg="lime")
run_button.grid(row=2, column=1, padx=10, pady=10)

# Create the status label
status_label = tk.Label(root, text="", fg="white", bg="gray10", font=("Arial", 12))
status_label.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
