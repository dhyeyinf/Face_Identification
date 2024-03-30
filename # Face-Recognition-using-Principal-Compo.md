# Face-Recognition-using-Principal-Component-Analysis

This repository contains a .ipynb file which contains the code for facial recognitation of PCA

### Objective:
We have created a basic facial recognition system using a technique called principal component analysis (PCA) 
by projecting the face images on the feature space (face space) which best
represents the variations among distinct faces. The face space is defined as the
“Eigenfaces", which are the eigenvectors of the set of faces.

The goal of implementing this system is to recognize a person's face by comparing it to a pre-existing database of faces, and identifying the closest match.


### About the dataset: 
The provided dataset is the deep funneled version of the original LFW dataset (Labelled Faces in the Wild dataset
with 13233 images of 5749 people), i.e., it includes images that have been aligned using various techniques to improve
face alignment and normalization. The brief dataset description can be found as follows:
- Image Information
  - File Format: Every file is a jpg file in the format: <person_name>_<image_count>, where image count is
in 4 digits ex: Winona_Ryder_0012.jpg to represent 12th image of Winona Ryder.
  - Slicing: Since these images are already pre-processed, no slicing needs to be done, i.e., the default slice
of each image is (slice(0, 250), slice(0, 250)) i.e., complete 250x250 pixels.
- Associated Metadata: Training and Testing datasets are provided in the form of various csv files (containing
the person name and image-no. of that person).

### Tasks Performed
1. Loading dataset and divide the date into training and test sets. 
2. Implement the PCA algorithm from scratch.
3. Implement image reconstruction using the eigen projections and visualise differences for different number of components.
4. Visualise the mean(Eigen face) generated.
5. Given training set, obtain accuracy by attempting a face regonition module and obtaining the accuracy for different number of principal components.



### Steps for Implementation of PCA Algorithm

1. **Standardize the data**: PCA is sensitive to the scale of the input data, so it is important to standardize the data to have zero mean and unit variance.

2. **Compute the covariance matrix**: Calculate the covariance matrix of the standardized data. This matrix shows how the different features of the data are related to each other.

3. **Compute the eigenvectors and eigenvalues of the covariance matrix**: The eigenvectors are the principal components, and the eigenvalues indicate the amount of variance explained by each principal component.

4. **Select the principal components**: Sort the eigenvectors by their corresponding eigenvalues in descending order, and select the top k eigenvectors to form the new lower-dimensional space. This new space will have k dimensions, where k is less than the original number of dimensions.


### Steps for Implementation of Image Reconstruction from Eigenfaces

1. **Load the image**: Load the image that you want to reconstruct.

2. **Vectorize the image**: Convert the grayscale image into a 1D vector.

3. **Standardize the data**

4. **Compute the eigenvectors and eigenvalue**s: Compute the eigenvectors and eigenvalues of the covariance matrix of the standardized vector.

5. **Select the principal components**: Choose the top k eigenvectors that explain the most variance in the data. This will be the lower-dimensional representation of the image.

6. **Project the image onto the lower-dimensional space**: Project the standardized vector onto the selected eigenvectors to obtain the lower-dimensional representation.

7. **Reconstruct the image**: Multiply the lower-dimensional representation by the selected eigenvectors and add the mean of the standardized vector to obtain the reconstructed image.




#### Advantages of using PCA in general and limitations of PCA in context of face recognitation.

**Answer:**

**Advantages**:

* Reduces the number of variables: PCA can help reduce the number of variables in a dataset while retaining the most important information. This can help simplify analysis and improve model performance.

* Increases interpretability: PCA transforms variables into a new set of variables that are uncorrelated and have a clear interpretation. This can help improve the interpretability of the data and make it easier to understand.

* Improves visualization: PCA can be used to visualize high-dimensional data in a lower-dimensional space, making it easier to see patterns and relationships.

**Limitations**:

* Assumes linear relationships: PCA assumes that the relationships between variables are linear. If there are non-linear relationships, PCA may not be appropriate.

* Can be sensitive to outliers: PCA can be sensitive to outliers, which can have a significant impact on the results.
Requires data scaling: PCA requires that variables be scaled to have the same variance, which can be problematic if variables have very different scales.

In the context of face recognition, PCA has some additional limitations:

* Limited ability to capture facial variations: PCA is not always able to capture the full range of facial variations, such as changes in lighting or expression, which can limit its effectiveness in face recognition applications.

* Limited accuracy: While PCA can be effective for face recognition in some situations, it is not always accurate enough for use in high-security applications where identification must be highly reliable.

* Limited ability to handle large datasets: PCA can be computationally expensive and may not be suitable for very large datasets.

