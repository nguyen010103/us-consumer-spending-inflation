import pandas as pd
import os

def drop_and_save(filename):
    """
    Load a CSV file, drop missing values and specific columns,
    then save the cleaned file to the 'processed' folder.
    """

    # Define input and output paths
    input_path = f'/Users/anhnguyendo/Documents/Python machine learning/US CPI project/us-consumer-spending-inflation/data/raw/{filename}'
    output_dir = '/Users/anhnguyendo/Documents/Python machine learning/US CPI project/us-consumer-spending-inflation/data/processed'
    os.makedirs(output_dir, exist_ok=True)
    
    # Load the data
    df = pd.read_csv(input_path)

    # Print initial shape and missing info
    print("Initial shape:", df.shape)
    print("Missing values per column:\n", df.isnull().sum())

    # Drop rows with missing values
    df_cleaned = df.dropna()

    # Drop specific columns (if they exist)
    df_cleaned = df_cleaned.drop(columns=['realtime_start','realtime_end'])

    # Save the cleaned file to the processed directory
    output_path = os.path.join(output_dir, f'{filename}_cleaned')  # Keep same filename
    df_cleaned.to_csv(output_path, index=False)

    print(f"Cleaned file saved to: {output_path}")


