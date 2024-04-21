import sys
import joblib
import numpy as np
from PIL import Image
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import csv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load LDA model
lda = joblib.load('lda_model.pkl')

# Load SVM model
svm_model = joblib.load('svm_model.pkl')

# Load unique labels
def load_unique_labels(csv_file):
    unique_labels_list = []
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            unique_labels_list = [row[0] for row in csv_reader]
    except FileNotFoundError:
        logging.error("CSV file '{}' not found.".format(csv_file))
    except Exception as e:
        logging.error("An error occurred while loading unique labels: {}".format(str(e)))
    return unique_labels_list

# Perform prediction
def predict(image_path, unique_labels):
    try:
        # Load and preprocess the uploaded image
        image = Image.open(image_path)
        resized_image = image.resize((50, 50))
        image_array = np.array(resized_image)
        flat_image_array = image_array.flatten()
        test_features = flat_image_array.reshape(1, -1)
        test_lda = lda.transform(test_features)

        # Predict using the loaded SVM model
        test_pred = svm_model.predict(test_lda).reshape(-1, 1)
        predicted_label = unique_labels[test_pred[0][0]]

        return predicted_label
    except FileNotFoundError:
        logging.error("Image file '{}' not found.".format(image_path))
    except Exception as e:
        logging.error("An error occurred during prediction: {}".format(str(e)))

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <image_path> <csv_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    csv_file = sys.argv[2]

    unique_labels_list = load_unique_labels(csv_file)
    if not unique_labels_list:
        logging.error("Failed to load unique labels. Exiting.")
        sys.exit(1)

    prediction = predict(image_path, unique_labels_list)
    if prediction:
        print(prediction)
    else:
        print("Prediction failed.")
