import streamlit as st
from datasets import load_dataset

# Create a Streamlit app
app = st.App()

# Add a title to the app
app.title("Dataset Formatter")

# Add a sidebar to the app
app.sidebar.header("Last 5 Generated Files")

# Add a text input field to the sidebar for the dataset name
dataset_name_input = app.sidebar.text_input("Enter the name of the dataset to load:", "")

# Add a text input field to the sidebar for the JSONL filename
jsonl_filename_input = app.sidebar.text_input("Enter the name of the .jsonl file to save:", "")

# Add a button to the sidebar to generate the formatted data
generate_button = app.sidebar.button("Generate Dataset")

# Define a function to format the data
def format_data(dataset_name, jsonl_filename):
    # Load the dataset
    ds = load_dataset(dataset_name, split='train')
    
    # Format the data
    formatted_data = []
    for sample in ds:
        formatted_data.append({"text": f"<<SYS>>\nCreate a description of a situation, person or object.\n<</SYS>>\n\nDescription:\n{sample['text']}"})
    
    # Save the formatted data to a JSONL file
    with open(f"datasets/{jsonl_filename}.jsonl", "w") as f:
        json.dump(formatted_data, f)

# Call the format_data function when the generate button is clicked
if generate_button.clicked():
    format_data(dataset_name_input.value, jsonl_filename_input.value)

# Display the formatted data in the main area of the app
app.main.write(f"Formatted Data: {formatted_data}")

# Run the app
if __name__ == "__main__":
    app.run()