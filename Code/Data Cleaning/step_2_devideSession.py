import os
import pandas as pd

# Folder containing Excel files
folder_path = "/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/processing"

# Function to split the dataframe into chunks
def split_dataframe(df, chunk_size):
    num_chunks = (len(df) + chunk_size - 1) // chunk_size
    chunks = [i for i in range(num_chunks) for _ in range(chunk_size)]
    chunks += [num_chunks - 1] * (len(df) % chunk_size)  # Handle remaining rows
    df['chunk'] = chunks[:len(df)]
    return df

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):  # Check if the file is an Excel file
        file_path = os.path.join(folder_path, filename)

        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name="Sheet1", engine="openpyxl")

        # Split the dataframe into chunks of 100 rows each
        df = split_dataframe(df, chunk_size=100)

        # Save the modified DataFrame back to the Excel file
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)

print("Task completed.")
