Supervised Learning
---

# Overview

- Supervised learning algorithms are trained using `labeled` examples, such as an input where the desired output is known.
- For example, a segment of text could have a catelogry label, such as:
    - `Spam` vs `Legitimate` Email
    - `Positive` vs `Negative` Movie Review
- The network receives a set of inputs along with the corresponding correct outputs, and the algorithm learns by comparing its actual output with correct outputs to find errors.
- It then modifies the model accordingly.

## Machine Learning Process

1. Data Acquisition
2. Data Cleaning
3. Split Data often into 3 sets
    - Training Data
        - 60%
        - Used to train the model
    - Validation Data 
        - 20%
        - Used to validate what model hyperparameters to adjust
    - Test Data
        - 20%
        - Used to get some final performance metric
4. Model Training & Building
5. Model Testing
    - If Positive
        - GoTo: Model Deployment
    - Else:
        - Adjust model parameters
        - GoTo Model Training & Building
6. Model Deployment
7. Model Evaluation
    - Correct Prediction
    - Incorrect prediction

### Evaluating Performance - Classification Error Metrics

- These metrics are ways to comparing the predicted values vs true values.
- What constitutes "good" metrics will really depend on the specific situation.

#### Classification Types

- Binary Classification
- Multiple Classification

#### Key Classifiacation Metrics

##### Accuracy

``Accuracy = Number of correct predictions / Total number of predictions``

- Useful when target classes are balanced. For eg: roughly same number of cat and dog impages
- Not good for unbalanced classes. For eg: 10 dogs and 90 cat images

##### Recall

``Recall Precision = Number of true positives / (Number of true postives + Number of false negatives)``

- Ability of a model to find all the relevant cases within a dataset

##### Precision

- Expresses the proportion of the data points our model says was relevant actually were relevant.
- Often you have trade-off between Recall and Precision.

##### F1-Score

``F1-Score = 2 * (precision * recall) / (precision + recall)``

- Harmonic mean of precision and recall
- Combination of Recall and Precision
- Helps you find the optimal blend of precision and recall by combinding these two metrics.

#### Confusion Matrix

- We can view all correctly classified versus incorrectly classified images in the form of a confusion metrix.

|    |       | Predicted  Condition | Predicted  Condition |
--  | --    | --            | --
|   | Total Population | Prediction Postive | Prediction Negative
True Condition | Condition Positive | True Positive (TP) | False Negative (FN) (type II error)
True Condition | Condition Negative | False Positive (FP) (type I error) |  True Negative (TN)

![Confusion Matrix](https://www.unite.ai/wp-content/uploads/2019/12/Preventive_Medicine-e1576294312614.png)

