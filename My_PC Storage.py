import os
import pandas as pd
from tkinter import Tk, filedialog

def get_file_info(directory):
    file_info = []

    # Traverse the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_info.append({'File Path': file_path, 'Size (bytes)': file_size})
    
    return file_info

def save_to_excel(file_info, output_file):
    df = pd.DataFrame(file_info)
    df.to_excel(output_file, index=False, engine='openpyxl')

def select_directory():
    root = Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Select Directory")
    return directory

def select_output_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("Excel files", "*.xlsx")],title="Save Excel File As")
    return file_path

if __name__ == "__main__":
    directory = select_directory()
    if not directory:
        print("No directory selected.")
    else:
        output_file = select_output_file()
        if not output_file:
            print("No output file selected.")
        else:
            if os.path.isdir(directory):
                file_info = get_file_info(directory)
                save_to_excel(file_info, output_file)
                print(f"Report saved to {output_file}")
            else:
                print("The selected path is not a valid directory.")
