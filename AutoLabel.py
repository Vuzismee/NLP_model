

import pandas as pd

# Read the CSV file with the appropriate encoding
file_path = 'Tweetstest.csv'
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='cp1252')

# Print out column names to debug
print("Column names:", df.columns)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Check if 'text' column exists
if 'text' not in df.columns:
    raise KeyError("The 'text' column is not found in the CSV file. Available columns are: " + ", ".join(df.columns))

# Define a function to label the data
def label_text(text):
    if pd.isna(text):
        return 'Other'
    
    text_lower = text.lower()
    if 'ddos' in text_lower:
        return 'DDoS'
    elif any(keyword in text_lower for keyword in ['down', 'is down', 'not accessible', 'unavailable', 'offline', 'outage', 'website crash', 'attack']):
        return 'Not sure'
    else:
        return 'Other'

# Apply the labeling function to the text column
df['label'] = df['text'].apply(label_text)

# Save the labeled data to a new CSV file
output_file_path = 'dataset.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8')

print(f"Labeled data saved to {output_file_path}")
