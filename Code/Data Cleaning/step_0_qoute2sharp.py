import os
import pandas as pd

# Define the folder containing Excel files
folder_path = '/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/processing'

# Function to process a single Excel file
def process_excel_file(file_path):
    # Read the Excel file
    try:
        df = pd.read_excel(file_path, sheet_name='Sheet1')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # Check if 'Utterance' column exists
    if 'Utterance' in df.columns:
        # Replace ' with #
        df['Utterance'] = df['Utterance'].str.replace("'", '#')
        # Replace -- with space
        df['Utterance'] = df['Utterance'].str.replace('--', ' ')
        # Replace [ with space
        df['Utterance'] = df['Utterance'].str.replace('[', ' ')
        # Replace ] with space
        df['Utterance'] = df['Utterance'].str.replace(']', ' ')

        # Save the modified data to the original Excel file
        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"Processed and saved: {file_path}")
    else:
        print(f"'Utterance' column not found in {file_path}")

# Loop through all Excel files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        process_excel_file(file_path)