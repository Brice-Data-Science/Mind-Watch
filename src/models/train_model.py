"""Train Model."""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd


def train_model(df):
    """Train a model to predict depression."""
    # Separate features and target
    X = df.drop(columns=['depression_diagnosis'])
    y = df['depression_diagnosis']

    # Train-test split
    X_train, X_test, y_train, y_test = (train_test_split(X, y, test_size=0.2,
                                                         random_state=42))

    # Train a Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", accuracy)

    return model


if __name__ == "__main__":
    # Load processed data
    df = pd.read_csv('data/processed/mental_health_survey_cleaned.csv')

    # Train and evaluate model
    model = train_model(df)
