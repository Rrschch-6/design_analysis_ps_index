import pandas as pd
import os

# Specify the folder containing Excel files
excel_folder = "/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/processing"

# Initialize a list to store message dictionaries for all chunks
all_messages = []

# Function to create a message dictionary
def create_message(chunk_df):
    system_message = {"role": "system", "content": "I am going to feed you a transcript. I want you to break it down and tag each segment. The available tags are as below: P: when the segment is a discussion about the problem or the problem space. S: when the segment is a discussion about the solution or the solution space. O: none of the above. Confirm and await for the transcript. start each line of your answer only with P: S: or O:"}
    user_message = {"role": "user", "content": " ".join(chunk_df['Utterance'].astype(str))}
    assistant_message = {"role": "assistant", "content": ""}
    
    # Iterate through lines in the chunk
    for index, row in chunk_df.iterrows():
        assistant_message["content"] += f"{row['p_s']}: {row['Utterance']}\n"
    
    return {"messages": [system_message, user_message, assistant_message]}

# Process each Excel file in the folder
for filename in os.listdir(excel_folder):
    if filename.endswith('.xlsx'):
        excel_path = os.path.join(excel_folder, filename)
        df = pd.read_excel(excel_path, sheet_name='Sheet1')

        # Group by 'chunk' column and create message dictionaries
        grouped = df.groupby('chunk')
        for chunk_value, chunk_df in grouped:
            message_dict = create_message(chunk_df)
            
            # Append the message dictionary to the list
            all_messages.append(message_dict)

# Create a DataFrame from all_messages list
all_messages_df = pd.DataFrame(all_messages)

# Save all messages in a single CSV file
output_csv_path = '/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/processing/final.csv'
all_messages_df.to_csv(output_csv_path, index=False)
