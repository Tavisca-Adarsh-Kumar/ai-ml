[Scikit Learn](https://scikit-learn.org/1.3/tutorial/)
---

# Introduction

- It is the most popular machine learning package for python.
- It has a lot of algorithms built-in.
- Every algorithm is exposed via an "Estimator"
- Importing Estimator: 
    - Syntax:   `from sklearn.family import Model`
    - Eg:       `from sklearn.linear_model import LinearRegression`
- Estimator
    - LinearRegression is the estimator object in above example
    - Estimator Paramters:
        - All the parameters of estimator can be set while it is instantiated, and have suitable default values.
        - Eg: `model = LinearRegression(normalize=True)`
- Split Data
    - Eg: `from sklearn.cross_validation import train_test_split`
          `X, y = np.arange(10).reshape((5, 2)), range(5)`
          `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)`
- Fit your model on data
    - Eg: `model.fit(X_train, y_train)`
- Predict the values
    - Eg: `predictions = model.predict(X_test)`
- Evaluate your model

## All Estimators

- `model.fit()` : fit training data
- Supervised: `model.fit(X, y)` where X is the data and y are the labels
- Unsupervised: `model.fit(X)` where X is the data

### Supervised Estimators

- `model.predict(X_new)` : give a trained model, predict the label of new data set. X_new is new data set. It returns the learned labels for each object in new data set.
- `model.predict_proba()`
    - For `classification problems`, some estimator provides this.
    - It returns the probability that a new observation has each categorical label.
    - In this case, the label with highest probability is returned by `model.predict()`.
- `model.score()`
    - For classification or regression problems, most estimators implement this.
    - Scores are between 0 and 1, with larger score indicating better fit.

### Unsupervised Estimators

- `model.predict()`
    - Predict labels in clustering algorithms.
- `model.transform(X_new)`
    - Given an unsupervised model, transform new data into the new basis.
    - It also accepts one argument X_new, and returns the new representation of the data based on the unsupervised model.
- `model.fit_transform()`
    - Some estimators implement this method.
    - It performs fit and and a transform on the same input data more efficiently.

# Choosing an Algorithm

![Choosing an Algorithm](https://scikit-learn.org/1.5/_downloads/b82bf6cd7438a351f19fac60fbc0d927/ml_map.svg)

