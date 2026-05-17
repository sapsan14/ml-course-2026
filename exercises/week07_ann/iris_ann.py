"""Iris ANN assignment module for autograder import."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
import tensorflow as tf

DATA_COLUMNS = ["sepal length", "sepal width", "petal length", "petal width", "class"]
INPUT_DIM = len(DATA_COLUMNS) - 1
TEST_SIZE = 0.3
RANDOM_STATE = 42

np.random.seed(RANDOM_STATE)

SUBMISSION_VERSION = "iris_ann_safe_import_v3"


def _get_tf_keras():
    """Lazy TensorFlow/Keras import for autograder import safety."""
    import tensorflow as tf
    from tensorflow.keras.layers import Dense, Input
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.utils import to_categorical

    return tf, Dense, Input, Sequential, to_categorical


def resolve_iris_data_path(filename="iris.data"):
    """Locate iris.data next to cwd or typical Google Colab Drive folders."""
    candidates = [
        Path(filename),
        Path.cwd() / filename,
        Path("/content/drive/MyDrive/Colab Notebooks") / filename,
        Path("/content/drive/My Drive/Colab Notebooks") / filename,
    ]
    for p in candidates:
        if p.is_file():
            return str(p)
    return str(Path.cwd() / filename)


def try_to_mount_drive():
    """Mount Google Drive. For local usage only."""
    try:
        from google.colab import drive
        import os

        drive.mount("/content/drive")
        os.chdir("/content/drive/My Drive/Colab Notebooks")
        return True
    except ImportError:
        return False


def read_data(filename):
    """Read the iris dataset with the correct column names."""
    path = Path(filename)
    if path.is_file():
        df = pd.read_csv(path, names=DATA_COLUMNS)
        df = df.dropna(how="any").reset_index(drop=True)
        return df

    if path.name == "iris.data":
        from sklearn.datasets import load_iris

        iris = load_iris(as_frame=True)
        X = iris.data.copy()
        X.columns = DATA_COLUMNS[:-1]
        class_map = {i: f"Iris-{name}" for i, name in enumerate(iris.target_names)}
        X["class"] = iris.target.map(class_map)
        return X

    raise FileNotFoundError(f"Dataset file not found: {filename}")


def encode_labels_to_numerical(data):
    """Encode the labels to numerical values. eg. iris_color to 0."""
    if "class" not in data.columns:
        raise ValueError("missing required column 'class'")

    le = LabelEncoder()
    data["class"] = le.fit_transform(data["class"].astype(str)).astype(np.int64)
    return data


def separate_features_and_labels(data):
    """Split the dataset into features and labels."""
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y


def encode_labels_as_one_hot(y, num_classes=3):
    """Encode labels to one-hot format."""
    y_arr = np.asarray(y).astype(np.int64)
    return to_categorical(y_arr, num_classes=num_classes).astype(np.float32)


def split_data_to_test_and_train(X, y):
    """Split the dataset into two for testing and validation."""
    y_labels = np.argmax(np.asarray(y), axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y_labels,
    )
    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """Standardize features using the training split as reference."""
    scaler = StandardScaler()
    X_train_np = np.asarray(X_train, dtype=np.float32)
    X_test_np = np.asarray(X_test, dtype=np.float32)
    X_train_scaled = scaler.fit_transform(X_train_np).astype(np.float32)
    X_test_scaled = scaler.transform(X_test_np).astype(np.float32)
    return X_train_scaled, X_test_scaled, scaler


def create_model():
    """Create a model with different layers."""
    _, Dense, Input, Sequential, _ = _get_tf_keras()
    model = Sequential(
        [
            Input(shape=(INPUT_DIM,)),
            Dense(16, activation="relu"),
            Dense(8, activation="relu"),
            Dense(3, activation="softmax"),
        ]
    )
    return model


def compile_model(model):
    """Compile model with loss, optimizer and metrics."""
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model


def train_model(model, X_train, X_test, y_train, y_test, epochs=150):
    """Train the model using training and testing datasets."""
    X_train = np.asarray(X_train, dtype=np.float32)
    X_test = np.asarray(X_test, dtype=np.float32)
    y_train = np.asarray(y_train, dtype=np.float32)
    y_test = np.asarray(y_test, dtype=np.float32)

    history = model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=16,
        verbose=0,
    )
    return history


def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return accuracy."""
    X_test = np.asarray(X_test, dtype=np.float32)
    y_test = np.asarray(y_test, dtype=np.float32)
    _, evaluation_accuracy = model.evaluate(X_test, y_test, verbose=0)
    return float(evaluation_accuracy)


def evaluate_using_predictions(model, X_test, y_test):
    """Evaluate accuracy by comparing predictions and expected labels."""
    X_test = np.asarray(X_test, dtype=np.float32)
    y_test = np.asarray(y_test, dtype=np.float32)
    probs = model.predict(X_test, verbose=0)
    y_pred = np.argmax(probs, axis=1)
    y_true = np.argmax(y_test, axis=1)
    return float(accuracy_score(y_true, y_pred))


def run_eda_overview(filename=None):
    """Run EDA prints manually without top-level side effects."""
    file_to_read = filename or resolve_iris_data_path()
    df = read_data(file_to_read)
    print("shape:", df.shape)
    print(df.head())
    print(df["class"].value_counts())
    print(df.describe())
    return df


def plot_eda_histograms(df):
    """Plot feature histograms for manual EDA."""
    import matplotlib.pyplot as plt

    feature_cols = DATA_COLUMNS[:-1]
    fig, axes = plt.subplots(2, 2, figsize=(9, 7))
    axes = axes.ravel()
    for ax, col in zip(axes, feature_cols):
        ax.hist(df[col], bins=15, color="steelblue", edgecolor="black", alpha=0.75)
        ax.set_title(col)
    plt.tight_layout()
    plt.show()

    print(
        "Tähelepanekud: klassid on tasakaalus (50+50+50). "
        "Petal mõõdud eristavad liike paremini kui sepal mõõdud — see peaks närvivõrgule sobima."
    )


def show_training_report(results):
    """Show loss curves and confusion matrix manually."""
    import matplotlib.pyplot as plt

    hist = results["history"].history
    plt.figure(figsize=(8, 4))
    plt.plot(hist["loss"], label="train loss")
    plt.plot(hist["val_loss"], label="val loss")
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.legend()
    plt.title("Mudeli kao (categorical_crossentropy)")
    plt.tight_layout()
    plt.show()

    y_prob = results["model"].predict(results["X_test_scaled"], verbose=0)
    y_pred = np.argmax(y_prob, axis=1)
    y_true = np.argmax(results["y_test"], axis=1)
    print("Confusion matrix (readout rows = true class, columns = predicted):")
    print(confusion_matrix(y_true, y_pred))
    print(classification_report(y_true, y_pred, digits=4))


SUBMISSION_VERSION = "iris_ann_safe_import_v3"

def main():
    """Run the full pipeline."""
    try_to_mount_drive()
    np.random.seed(RANDOM_STATE)
    tf.random.set_seed(RANDOM_STATE)
    tf.keras.backend.clear_session()

    iris_file = resolve_iris_data_path()
    data = read_data(iris_file)

    encoded_data = encode_labels_to_numerical(data)
    X, y = separate_features_and_labels(encoded_data)
    y_one_hot = encode_labels_as_one_hot(y, num_classes=3)

    X_train, X_test, y_train, y_test = split_data_to_test_and_train(X, y_one_hot)
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)

    model = create_model()
    model = compile_model(model)
    history = train_model(model, X_train_scaled, X_test_scaled, y_train, y_test, epochs=150)

    evaluation_accuracy = evaluate_model(model, X_test_scaled, y_test)
    prediction_accuracy = evaluate_using_predictions(model, X_test_scaled, y_test)

    return {
        "evaluation_accuracy": evaluation_accuracy,
        "prediction_accuracy": prediction_accuracy,
        "history": history,
        "model": model,
        "X_test_scaled": X_test_scaled,
        "y_test": y_test,
        "data": data,
        "scaler": scaler,
    }


if __name__ == "__main__":
    results = main()
    print(f"Evaluation accuracy: {results['evaluation_accuracy']:.4f}")
    print(f"Prediction accuracy: {results['prediction_accuracy']:.4f}")
