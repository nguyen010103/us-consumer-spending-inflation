def drop_and_save(filename):
    import pandas as pd
    import os

    input_path = f'/Users/anhnguyendo/Documents/Python machine learning/US CPI project/us-consumer-spending-inflation/data/raw/{filename}'
    output_dir = '/Users/anhnguyendo/Documents/Python machine learning/US CPI project/us-consumer-spending-inflation/data/processed'
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)

    print("Initial shape:", df.shape)
    print("Missing values per column:\n", df.isnull().sum())

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    df_cleaned = df.dropna()

    for col in ['realtime_start', 'realtime_end']:
        if col in df_cleaned.columns:
            df_cleaned.drop(columns=[col], inplace=True)

    base_name = os.path.splitext(filename)[0]
    output_path = os.path.join(output_dir, f"{base_name}_cleaned.csv")

    df_cleaned.to_csv(output_path, index=False)
    print(f"✅ Cleaned file saved to: {output_path}")




