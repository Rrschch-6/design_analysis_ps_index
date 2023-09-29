import os
import pandas as pd

# Folder containing Excel files
folder_path = "/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/processing"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):  # Check if the file is an Excel file
        file_path = os.path.join(folder_path, filename)

        # Read the Excel file
        df = pd.read_excel(file_path, engine="openpyxl")

        # Add a new column "p_s" based on the "Code" column
        df['p_s'] = df['Code'].apply(lambda x: 'P' if x in ['R', 'F', 'Be'] else ('S' if x in ['S', 'Bs'] else 'O'))

        # Save the modified DataFrame back to the Excel file
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)

print("Task completed.")
