import pandas as pd

def load_data(filepath):
    """
    Load CSV data from the given filepath.
    
    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    df = pd.read_csv(filepath)
    return df[df['nav'] > 0]