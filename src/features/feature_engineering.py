"""Feature Engineering."""

import pandas as pd


def load_raw_data(filepath):
    """Load raw data from a CSV file."""
    return pd.read_csv(filepath)


def preprocess_data(df):
    """
    Found basic data preprocessing: handle missing values, encode categorical.

    variables, etc.
    """
    # Example: Drop rows with missing values in critical columns
    df = df.dropna(subset=['age', 'depression_diagnosis'])
    # Encode categorical variables
    df = pd.get_dummies(df, drop_first=True)
    return df


if __name__ == "__main__":
    # Load raw data
    filepath = (r'..data/raw/train.csv')
    df = load_raw_data(filepath)

    # Process data
    df_processed = preprocess_data(df)

    # Save processed data
    df_processed.to_csv('data/processed/mental_health_survey_cleaned.csv',
                        index=False)
