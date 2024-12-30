Introduction
---

# Artificial Intelligence (AI)

- Capability of machines to perform activities using human-like intelligence.


## Machine Learning (ML)

- It is how computers learn from data to discover patterns and make predictions.
- ML = Applied Math + Statistics + Computer Science

### Machine Learning Techniques

#### Supervised Learning

- Every training sample from the dataset has a corresponding label or output value associated with it.
- Algorithm learns to predict labels or output values.
- Usecases:
    - Predict housing prices in a neighborhood based on lot size and number of bedrooms

##### Classification

##### Regression

- Multiple regression
- Univariate regression
- multivariate regression

#### Unsupervised Learning

- No labels for the training data.
- Algorithm tries to learn the underlying patterns or distributions that govern the data.
- Models:
    - K-Means
- Usecases:
    - Isolate micro-genres of books by analyzing the wording on the back cover description.

##### Cluster

##### Dimentionality Reduction

#### Semi Supervised Learning

- Combinations of unsupervised and supervised algorithms

#### Self-supervised Learning

- Involves actually generating a fully labeled dataset from a fully unlabeled one.
- Uses (generated) labels during training, so in that regard it’s closer to supervised learning compared to unsupervised.

#### Reenforcement Learning

- Algorithm figures out which actions to take in a situation to maximize a reward (in the form of a number) on the way to reaching a specific goal.
- Usecases:
    - Analyze raw images from lab video footage from security cameras, trying to detect chemical spills.

##### Trial & Error

##### Deep Learning

- Transfer learning
    - Transferring knowledge from one task to another

### Machine Learning Components

#### Machine Learning Model

- Generic program made specific by data
- A block of code used to solve different problems
- Example:
    - Linear regression model

#### Model Training Algorithm

- Iterative process
    - Computes model's results on data
    - Makes small changes to the model to make the results better

#### Model Inference Algorithm

- Process to use a trained model to solve a task
- Using a trained model to generate predictions

### Machine Learning Steps

#### Step 1: Define the Problem

- Be specific!

##### Machine Learning Task

- Supervised Learning Task

    - Involves labeled data where the solution is known
    - Labels can be
        - Categorical Label (Classification)
        - Continous Label (Regression)
        - ...

- Unsupervised Learning Task

    - Involves the unlabed data where solution is not known
    - Task Types:
        - Clustering
        - ...

#### Step 2: Build the Dataset

- Time spent on building the dataset: 80%

##### Aspects of working with data

- Data collection
    - Find and collect the data related to the problem you have defined
    - Supervised Learning - Labeled Data
    - Unsupervised Learning - Unlabeled Data

- Data Inspection
    - Explore your data looking for:
        - Outliers
        - Missing or incomplete data
        - Transform your data

- Summary Statistics
    - can help you identify:
        - Trends in the data
        - Scale of the data
        - Shape of the data

- Data Visualization
    - Great data visualizations communicate the findings to project stakeholders

#### Step 3: Train the Model

- Split the dataset;
    - `Training Dataset`: 80% data should be used for training the model
    - `Test Dataset`: 20% data should be used for evaluating the model
- Model training algorithm iteratively updates the `model parameters` to minimize some `loss function`.
    - Model Parameters:
        - Configuration that change how the model behaves
    - Hyperparameters:
        - Settings on the model which are not changed during training but can affect how quickly or how reliably the model trains, such as the number of clusters the model should identify.
    - Loss Function:
        - Measurement of how close the model is to its goal
- End to end training process:
    - Feed the training data into the model
    - Compute the loss function on the results
    - Update the model parameters in a direction that reduces loss
- Some of model examples:
    - Linear models
    - Tree-based models
    - Deep learning models
        - Feed Forward Neural Network (FFNN)
            - Structures neurons in a series of layers, with each neuron in a layer containing weights to all neurons in the previous layer.
        - Convolutional Neural Networks (CNN)
            - Represent nested filters over grid-organized data.
            - Most commonly used type of model when processing images.
        - Recurrent Neural Networks (RNN) and the related Long Short-Term Memory (LSTM)
            - Structured to effectively represent for loops in traditional computing, collecting state while iterating over some object.
            - Can be used for processing sequences of data.
        - Transformer
            - Modern replacement for RNN/LSTMs
            - Transformer architecture enables training over larger datasets involving sequences of data.

#### Step 4: Evaluate the Model

- Iterative Process
- Metrics are tailored to use cases

##### Metrics for evalution

- Model Accuracy
    - Fraction of predictions a model gets right.
- Mean Absolute Error (MAE)
    - Measured by taking the average of the absolute difference between the actual values and the predictions.
    - Ideally, this difference is minimal.
- Root Mean Square Error (RMSE)
    - Similar to MAE, but takes a slightly modified approach so values with large error receive a higher penalty.
    - Takes the square root of the average squared difference between the prediction and the actual value.
- Precision
- F1 Score
- Recall
- Log Loss
    - Seeks to calculate how uncertain your model is about the predictions it is generating.
- Hinge Loss
- R² (R^2)
    - Measures how well-observed outcomes are actually predicted by the model, based on the proportion of total variation of outcomes.
- KL Divergence
- Quantile Loss
- V Measure
- Rand Index
- Contingency Metrix
- Davies-Bouldin Index
- Fowlkes-Mallows
- Homogeneity
- Mutual Information
- Pair Confusion Matrix
- Calinski-Harabasz Index
- Completeness
- Silhouette Coefficent
    - How well was your data clustered
- Manual Inspection

#### Step 5: Inference - Use the Model

- Use your model to solve real problems
- Monitor the results


