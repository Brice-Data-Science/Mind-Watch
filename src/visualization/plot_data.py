"""Plot Data."""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_correlation_matrix(df):
    """Plot correlation matrix for the dataset."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix of Mental Health Survey Features")
    plt.show()


if __name__ == "__main__":
    # Load processed data
    df = pd.read_csv('data/processed/mental_health_survey_cleaned.csv')

    # Plot correlation matrix
    plot_correlation_matrix(df)
