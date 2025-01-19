Machine Learning Fundamentals
---
- Machine Learning = Data Science ∩ Software Engineering
- It is based on mathematical and statistical techniques
- High level steps:
    - Explore and prepare the data (Data Scientist)
    - Train a machine learning model
    - Integrate model into applications
    - Inferencing (predictions)

# Machine Learning Types

## Supervised Learning

- Training data includes both feature values and known label values.
- Key elements of training process:
    - Split the training data (randomly)
    - Tain the model using training data
    - Test model using validation data
    - Compare predictions with validate data
    - Calculate a metric for accuracy

### Regression

- The `label` predicted by the model is a `numeric value`.
- Algorithms
    - Linear Regression

#### Evaluation Metrics

> Consider the ice-cream sell forcasing use case to understand these metrics. Variances are 2,3,3,1,2,3.

##### Mean Absolute Error (MAE)

- Variance (v) indicates by what number each prediction was wrong.
- It doesn't matter if the prediction was `over or under the actual value`.
- MAE = mean(v1 + v2 + ... + vn)
-Eg: (2 + 3 + 3 + 1 + 2 + 3) / 6 = (14 / 6) = 2.33

##### Mean Squared Erros (MSE)

- It takes all discrepancies between predicted and actual labels into account equally.
- It may be more desirable to have a model that is consistently wrong by a small amount than one that makes fewer, but larger errors.
- One way to produce a metric that "amplifies" larger errors by squaring the individual errors and calculating the mean of the squared values.
- MSE = mean(v1^2 + v2^2 + v3^2 + ... + vn^2)
- Eg: (4 + 9 + 9 + 1 + 4 + 9) / 6 = 36 / 6 = 6 (score)

##### Root Mean Squared Errors (RMSE)

-  MSE calculates just a numeric score that indicates the level of error in the validation predictions.
- If we want to measure the error in terms of the number of ice creams, we need to calculate the square root of the MSE; which is RMSE.
- RMSE =  √mean(v1^2 + v2^2 + v3^2 + ... + vn^2)
- Eg: √((4 + 9 + 9 + 1 + 4 + 9) / 6) = √(36 / 6) = √6 = 2.45 (ice-creams)

##### Coefficient of determination (R<sup>2</sup> / R-Squared)

- All above metrics compare discrepencies between actual and predicted values.
- R-Squared is a metric that measures the proportion of variance in the validation results that can be explained by the model, as opposed to some anomalous aspect of the validation data.
- For eg: a day with a highly unusual number of ice creams sales because of a local festival.
- It compares the sum of squared differences between predicted and actual labels with the sum of squared differences between the actual label values and the mean of actual label values
- R2 = 1- ∑(y-ŷ)<sup>2</sup> ÷ ∑(y-ȳ)<sup>2</sup>
    - y: predicted label
    - ŷ: actual label
    - ȳ: mean of actual label
- The result is a value between 0 and 1 that describes the proportion of variance explained by the model.
- The `closer to 1 this value is, the better the model is fitting` the validation data.
- Eg: For ice-cream model, R-Squared = 0.95

### Classification

- The `label` represents a `categorization, or class`.

#### Binary Classification

- Predict one of `two mutually exclusive outcomes`.
- Probability is measured as a value between 0.0 and 1.0, such that the total probability for all possible classes is 1.0
- For eg, if the probability of a patient having diabetes is 0.7, then there's a corresponding probability of 0.3 that the patient isn't diabetic.
- Alorithms like `Logistic Regression` derives a sigmoid (S-shaped) function with values between 0.0 and 1.0
- The sigmoid describes the probability distribution so that plotting a value of x on the line identifies the corresponding probability that y is 1.
- Horizontal line indicates the threshold at which a model based on this function will predict true (1) or false (0).
- The threshold lies at the mid-point for y (P(y) = 0.5).
- For any values at this point or above, the model will predict true (1); while for any values below this point it will predict false (0). For example, for a patient with a blood glucose level of 90, the function would result in a probability value of 0.9.
- Since 0.9 is higher than the threshold of 0.5, the model would predict true (1) - in other words, the patient is predicted to have diabetes.

> Lets consider the diabetic example to predict if patient is diabetic.

##### Confusion Metrics

- It shows the prediction totals

.   | .     | ŷ             | ŷ
--  | --    |--             | --
.   | .     | 0             | 1 
y   | 0     | **2** (TN)    | 0 (FP)
y   | 1     | 1 (FN)        | **3** (TP)

##### Evaluation Metrics

###### Accuracy

- Accuracy - (TN + TP) ÷ (TN + FN + FP + TP)
- Eg: Accuracy = (2 + 3) ÷ (2 + 1 + 0 + 3) = 5 ÷ 6 = 0.83
    - Model produced correct predictions 83% of the time.
- It might initially seem like a good metric to evaluate a model, but there are many aspects to consider like suppose 11% of the population has diabetes.

###### Recall (True Positive Rate (TPR))

- It measures the proportion of positive cases that the model identified correctly. In other words, compared to the number of patients who have diabetes, how many did the model predict to have diabetes?

- Recall = TP ÷ (TP + FN)
- Eg: Recall = 3 ÷ (3 + 1) = 3 ÷ 4 = 0.75
    - It correctly identified 75% of patients who have diabetes as having diabetes.

###### Precision

- Similar to recall, but measures the proportion of predicted positive cases where the true label is actually positive.
- What proportion of the patients predicted by the model to have diabetes actually have diabetes?
- Precision = TP ÷ (TP + FP)
- Eg: Precision = 3 ÷ (3 + 0) = 3 ÷ 3 = 1.0
    - 100% of the patients predicted by our model to have diabetes do in fact have diabetes.

###### F1 Score

- An overall metric that `combined recall and precision`.
- F1 Score = (2 x Precision x Recall) ÷ (Precision + Recall)
- Eg: F1 Score = (2 x 1.0 x 0.75) ÷ (1.0 + 0.75) = 1.5 ÷ 1.75 = 0.86

##### Area Under the Curve (AUC)

- Metrics are often used to evaluate a model by plotting a received operator characteristic (ROC) curve that compares the TPR and FPR for every possible threshold value between 0.0 and 1.0:
- The ROC curve for a perfect model would go straight up the TPR axis on the left and then across the FPR axis at the top.
- Since the plot area for the curve measures 1x1, the area under this perfect curve would be 1.0 (meaning that the model is correct 100% of the time).
- A diagonal line from the bottom-left to the top-right represents the results that would be achieved by randomly guessing a binary label; producing an area under the curve of 0.5.
- Given two possible class labels, you could reasonably expect to guess correctly 50% of the time.
- AUC > 0.5 indicates that the model performs better at predicting than randomly guessing.

#### Multiclass Classification

- Predict a label that represents one of `multiple possible classes`.
- Used to `calculate probability` values for multiple class labels, enabling a model to predict the most probable class for a given observation.

##### Algorithms

###### One-vs-Rest (OvR) algorithms

- It train a `binary classification function for each class`, each calculating the probability that the observation is an example of the target class.
- Each function calculates the probability of the observation being a specific class compared to any other class.
- For our penguin species classification model, the algorithm would essentially create three binary classification functions:
    - f0(x) = P(y=0 | x)
    - f1(x) = P(y=1 | x)
    - f2(x) = P(y=2 | x)
- Each algorithm produces a sigmoid function that calculates a probability value between 0.0 and 1.0.
- A model trained using this kind of algorithm predicts the class for the function that produces the highest probability output.

###### Multinomial algorithms

- It creates a `single function` that returns a multi-valued output. The output is a vector (an array of values) that contains the probability distribution for all possible classes - with a probability score for each class which when totaled add up to 1.0.
- f(x) =[P(y=0|x), P(y=1|x), P(y=2|x)]
- Eg: `softmax function`, which could produce an output like: [0.2, 0.3, 0.5]
- The elements in the vector represent the probabilities for classes 0, 1, and 2 respectively; so in this case, the class with the highest probability is 2.
- Regardless of which type of algorithm is used, the model uses the resulting function to determine the most probable class for a given set of features (x) and predicts the corresponding class label (y).

##### Evaluation

- You can evaluate a multiclass classifier by calculating binary classification metrics for each individual class.
- Alternatively, you can calculate aggregate metrics that take all classes into account.
- We can create confusion matrix multiclass classifier similar to binary classifier.
- To calculate the overall accuracy, recall, and precision metrics, you use the total of the TP, TN, FP, and FN metrics:
    - Overall accuracy = (13+6)÷(13+6+1+1) = 0.90
    - Overall recall = 6÷(6+1) = 0.86
    - Overall precision = 6÷(6+1) = 0.86
- Overall F1-score is calculated using the overall recall and precision metrics:
    - Overall F1-score = (2x0.86x0.86)÷(0.86+0.86) = 0.86

## UnSupervised Learning

- It involves training models using data that consists `only of feature values without any known labels`.
- It determine relationships between the features of the observations in the training data.

### Clustering

- It `identifies similarities between observations` based on their features, and groups them into discrete clusters.
- Observations are `grouped into clusters based on similarities` in their data values, or features.
- Eg: Identify the species of flower

#### Training Clustering Model Algorithms

##### K-Means clustering

- The feature (x) values are vectorized to define n-dimensional coordinates (where n is the number of features).
- In the flower example, we have two features: number of leaves (x1) and number of petals (x2). So, the feature vector has two coordinates that we can use to conceptually plot the data points in two-dimensional space ([x1,x2])
- You decide how many clusters you want to use to group the flowers - call this value k.
- For example, to create three clusters, you would use a k value of 3. Then k points are plotted at random coordinates.
- These points become the center points for each cluster, so they're called `centroids`.
- Each data point (in this case a flower) is assigned to its nearest centroid.
- Each centroid is moved to the center of the data points assigned to it based on the mean distance between the points.
- After the centroid is moved, the data points may now be closer to a different centroid, so the data points are reassigned to clusters based on the new closest centroid.
- The centroid movement and cluster reallocation steps are repeated until the clusters become stable or a predetermined maximum number of iterations is reached.

#### Evaluating Clustering Model

- Evaluation of a clustering model is based on `how well the resulting clusters are separated` from one another.

##### Metrics

###### Average distance to cluster center

- How close, on average, each point in the cluster is to the centroid of the cluster.

###### Average distance to other center

- How close, on average, each point in the cluster is to the centroid of all other clusters.
    
###### Maximum distance to cluster center

- The furthest distance between a point in the cluster and its centroid.

###### Silhouette

- A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster separation).

## Deep Learning

- An advanced form of machine learning that `tries to emulate the way the human brain learns`.
- The key to deep learning is the creation of an artificial neural network that simulates electrochemical activity in biological neurons by using mathematical functions.
- Models produced by it are often referred to as `deep neural networks (DNNs)`.

### Model Architecture

#### Convolutional Neural Networks (CNNs)

- A type of deep learning architecture.
- It `use filters to extract numeric feature maps from images`, and then feed the feature values into a deep learning model to generate a label prediction.
- For example, in an image classification scenario, the label represents the main subject of the image (in other words, what is this an image of?).
- You might train a CNN model with images of different kinds of fruit (such as apple, banana, and orange) so that the label that is predicted is the type of fruit in a given image.
- During the training process for a CNN, filter kernels are initially defined using randomly generated weight values.
- Then, as the training process progresses, the models predictions are evaluated against known label values, and the filter weights are adjusted to improve accuracy.
- Eventually, the trained fruit image classification model uses the filter weights that best extract features that help identify different kinds of fruit.
Transformers and multi-modal models
- It is commonly used to solve image classification problems as described previously, they're also the basis for more complex computer vision models.
- For example, object detection models combine CNN feature extraction layers with the identification of regions of interest in images to locate multiple classes of object in the same image.

#### Transformers

- Used with Natural language processing (NLP)
- It work by processing huge volumes of data, and encoding language tokens (representing individual words or phrases) as vector-based embeddings (arrays of numeric values).
- You can think of an embedding as representing a set of dimensions that each represent some semantic attribute of the token.
- The embeddings are created such that tokens that are commonly used in the same context are closer together dimensionally than unrelated words.
- Tokens that are semantically similar are encoded in similar positions, creating a semantic language model that makes it possible to build sophisticated NLP solutions for text analysis, translation, language generation, and other tasks.

### Multi-modal models

The success of transformers as a way to build language models has led AI researchers to consider whether the same approach would be effective for image data. The result is the development of multi-modal models, in which the model is trained using a large volume of captioned images, with no fixed labels. An image encoder extracts features from images based on pixel values and combines them with text embeddings created by a language encoder. The overall model encapsulates relationships between natural language token embeddings and image features.
