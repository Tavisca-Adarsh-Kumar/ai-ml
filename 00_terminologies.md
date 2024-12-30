Terminologies
---

# A

## Action

For every state, an agent needs to take an action toward achieving its goal.

## Action Space

- Set of all `valid actions` or choices, available to an agent as it interact with an environment.

- Discrete Action
    - Finite set of possible actions

- Continous Action
    - Range of possible actions

## Agent

The piece of software you are training is called an agent. It makes decisions in an environment to reach a goal.

## Algorithm

- A set of instructions.
- A training algorithm tells the model to gather as many rewards as possible.

## Association Rule Learning

Goal is to dig into large amounts of data and discover interesting relations between attributes.

# B

## Bag of words

A technique used to extract features from the text. It counts how many times a word appears in a document (corpus), and then transforms that information into a dataset.

# C

## Categorical Label

It has a discrete set of possible values, such as "is a cat" and "is not a cat."

## Clustering

Unsupervised learning task that helps to determine if there are any naturally occurring groupings in the data.

## CNN

Convolutional Neural Networks (CNN) represent nested filters over grid-organized data. They are by far the most commonly used type of model when processing images.

## Continuous (Regression) Label

It does not have a discrete set of possible values, which means possibly an unlimited number of possibilities.

# D

## Data Pipeline

A sequence of data processing components.

## Data vectorization

A process that converts non-numeric data into a numerical format so that it can be used by a machine learning model.

## Discrete

A term taken from statistics referring to an outcome taking on only a finite number of values (such as days of the week).

## Discriminator

A neural network trained to differentiate between real and synthetic data.

## Discriminator Loss

Evaluates how well the discriminator differentiates between real and fake data.

## Dimensionality Reduction

The goal is to `simplify the data without losing too much information`. One way to do this is to merge several correlated features into one.

# E

## Environment

The environment is the surrounding area with which the agent interacts.

## Episode

Represents a period of trial and error when an agent makes decisions and gets feedback from its environment.

## Exploration versus exploitation

An agent should exploit known information from previous experiences to achieve higher cumulative rewards, but it also needs to explore to gain new experiences that can be used in choosing the best actions in the future.

# F

# Feature Engineering

- Coming up with a good set of features to train on.
- Involves the following steps:
    - Feature selection (selecting the most useful features to train on among existing features)
    - Feature extraction (combining existing features to produce a more useful one⁠—as we saw earlier, dimensionality reduction algorithms can help)
    - Creating new features by gathering new data

## Feedback

Given to an agent for each action it takes in a given state. This feedback is `numerical reward`.

## FFNN

The most straightforward way of structuring a neural network, the Feed Forward Neural Network (FFNN) structures neurons in a series of layers, with each neuron in a layer containing weights to all neurons in the previous layer.

# G

## Generator

A neural network that learns to create new data resembling the source data on which it was trained.

## Generator loss

Measures how far the output data deviates from the real data present in the training dataset.

# H

## Hyperparameters

- A parameter of a learning algorithm (not of the model).
- Settings/variables on the algorithm that controls performance of agent during training
- Not changed during training but can affect how quickly or how reliably the model trains, such as the number of clusters the model should identify.
- Examples:
    - Learning Rate
        - Controls how many new experiences are counted in learning at each step.

## Hyperplane

A mathematical term for a surface that contains more than two planes.

# I

## Impute

A common term referring to different statistical tools which can be used to calculate missing values from your dataset.

## Instance-based Learning

The system learns the examples by heart, then generalizes to new cases by using a similarity measure to compare them to the learned examples (or a subset of them).

# L

## Label

Refers to data that already contains the solution.

## Log Loss

Used to calculate how uncertain your model is about the predictions it is generating.

## Long Short-Term Memory (LSTM)

Such model types are structured to effectively represent for loops in traditional computing, collecting state while iterating over some object. They can be used for processing sequences of data.

## Loss Function

Used to codify the model’s distance from this goal

# M

## Machine Learning (ML)

A modern software development technique that enables computers to solve problems by using examples of real-world data.

## Model Accuracy

The fraction of predictions a model gets right. 

### Discrete

A term taken from statistics referring to an outcome taking on only a finite number of values (such as days of the week).

### Continuous

Floating-point values with an infinite range of possible values. The opposite of categorical or discrete values, which take on a limited number of possible values.

## Model Inference

It is when the trained model is used to generate predictions.

## Model

An extremely generic program, made specific by the data used to train it.

## Model-based Learning

- Build a model of examples and then use that model to make predictions.

## Model Parameters

Settings or configurations the training algorithm can update to change how the model behaves.

## Model Training Algorithms

Work through an interactive process where the current model iteration is analyzed to determine what changes can be made to get closer to the goal. Those changes are made and the iteration continues until the model is evaluated to meet the goals.

# N

## Neural Networks

A collection of very simple models connected together. These simple models are called neurons. The connections between these models are trainable model parameters called weights.

# O

## Online Learning

- Train the system incrementally by feeding it data instances sequentially, either individually or in small groups called mini-batches.
- Each learning step is fast and cheap, so the system can learn about new data on the fly, as it arrives.

## Outliers

Data points that are significantly different from others in the same sample.

## Overfitting (Overgeneralizing)

- Model performs well on the training data, but it does not generalize well.
- It happens when the model is too complex relative to the amount and noisiness of the training data.

# P

## Plane

A mathematical term for a flat surface (like a piece of paper) on which two points can be joined by a straight line.

# R

## Regression

A common task in supervised machine learning.

## Regularization

- Constraining a model to make it simpler and reduce the risk of overfitting.
- The amount of regularization to apply during learning can be controlled by a `hyperparameter`.

## Reinforcement Learning

The algorithm figures out which actions to take in a situation to maximize a reward (in the form of a number) on the way to reaching a specific goal.

## Reward

Feedback is given to an agent for each action it takes in a given state. This feedback is a numerical reward.

## Reward Function

- A tool for designing an incentive plan that will encourage your agent to reach its goal.

## RNN/LSTM: Recurrent Neural Networks (RNN)

Such model types are structured to effectively represent for loops in traditional computing, collecting state while iterating over some object. They can be used for processing sequences of data.

# S

## Sampling Noise

- If the sample is too small, you will have sampling noise 

## Sampling Bias

- Very large samples can be nonrepresentative if the sampling method is flawed.

## Silhouette Coefficient

A score from -1 to 1 describing the clusters found during modeling. A score near zero indicates overlapping clusters, and scores less than zero indicate data points assigned to incorrect clusters. A

## State

Defined by the `current position` within the environment that is visible, or known, to an agent.

## Stop Words

A list of words removed by natural language processing tools when building your dataset. There is no single universal list of stop words used by all-natural language processing tools.

# Stratified Sampling

The population is divided into homogeneous subgroups called strata, and the right number of instances are sampled from each stratum to guarantee that the test set is representative of the overall population.

## Supervised Learning

Every training sample from the dataset has a corresponding label or output value associated with it. As a result, the algorithm learns to predict labels or output values.

# T

## Test Dataset

The data withheld from the model during training, which is used to test how well your model will generalize to new data.

## Training Dataset

The data on which the model will be trained. Most of your data will be here.

## Transformer

A more modern replacement for RNN/LSTMs, the transformer architecture enables training over larger datasets involving sequences of data.

# U

## Underfitting

- Occurs when your model is too simple to learn the underlying structure of the data.

## Unlabeled Data

You don't need to provide the model with any kind of label or solution while the model is being trained.

## Unsupervised Learning

There are no labels for the training data. A machine learning algorithm tries to learn the underlying patterns or distributions that govern the data.
