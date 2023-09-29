import streamlit as st
import docx2txt
import io
import pandas as pd
from gpt_api_calls import inference,visualize
import matplotlib.pyplot as plt

# Streamlit app title
st.title("PS Index Analysis")

# Upload a Word document
uploaded_file = st.file_uploader("Upload Transcript", type=["docx"])

# Initialize the inference_done flag
inference_done = False
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
df1 = pd.DataFrame()
df2 = pd.DataFrame()

# Create a button to start inference
if st.button("Start Inference") and uploaded_file is not None:
    # Read the uploaded Word document and extract the text
    transcript = docx2txt.process(uploaded_file)

    # Call the inference function with the document text
    description = """Your description here"""  # Update this with your description
    df1 = inference(description, transcript, "gpt-4") 
    df2 = inference(description, transcript, "ft:gpt-3.5-turbo-0613:personal:psindex50-bot:83Y3pUzc")

    # Set the flag to indicate that inference is done
    inference_done = True

# Add download buttons for df1 and df2

    st.write("Inference done! You can now download the results as Excel files.")

    st.header("Result Comparison")
    # Call the visualize function with appropriate data
    baseline_ps_list=[91,24,18,27]
    fig = visualize()  # Call the visualize function
    # Display the Matplotlib figure using Streamlit
    st.pyplot(fig)
st.header("Result Download")
st.download_button("Download gpt4 result", df1.to_csv(index=False).encode('utf-8'),mime="text/csv",file_name="gpt4_result.csv")
st.download_button("Download gpt3.5 fine-tuned result",df2.to_csv(index=False).encode('utf-8'),mime="text/csv",file_name="gpt3.5_fine_tuned_result.csv")
image = "/mnt/d/Users/BKU/SashaBehrouzi/Documents/DPA/Data/download.png"  # Replace with the actual path to your image

# Display the image
st.image(image, caption="Your Image Caption", use_column_width=False, width=1200)