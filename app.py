from flask import Flask, request, render_template
import joblib
import numpy as np
from PIL import Image
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import csv

app = Flask(__name__)

# Load LDA model
lda = joblib.load('lda_model.pkl')

# Load SVM model
svm_model = joblib.load('svm_model.pkl')

# Load unique labels
with open('unique_labels.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    unique_labels_list = [row[0] for row in reader]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['image']
        
        # Load and preprocess the uploaded image
        image = Image.open(uploaded_file)
        resized_image = image.resize((50, 50))
        image_array = np.array(resized_image)
        flat_image_array = image_array.flatten()
        test_features = flat_image_array.reshape(1, -1)
        test_lda = lda.transform(test_features)

        # Predict using the loaded SVM model
        test_pred = svm_model.predict(test_lda).reshape(-1, 1)

        # Get the label corresponding to the prediction
        with open('unique_labels.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            unique_labels_list = [row[0] for row in reader]
        
        prediction_label = unique_labels_list[test_pred[0][0]]

        # Return the prediction to the client side
        return prediction_label

@app.route('/redirect')
def redirect_page():
    # Here, let's render another HTML page named 'new_page.html'
    return render_template('new_page.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
