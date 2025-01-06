Artificial Neural Network (ANN)
---

## Perceptron Modal

### Equation

`y = (x1w1  + b) + (x2w2 + b) + ... + (xnwn + b)`

- y is result
- x1, x2, ..., xn are inputs
- w1, w2, ..., wn are weights
- b is bias
- Capital letters like X, Z indicates the value consisting of multiple values.

### Components of Perceptron Modal

- Dendrites (Input)
- Nucleus (Function)
- Axon (Output)

## Neural Networks

- To build a network of perceptrons, we can connect layers of perceptrons, using a `multi-layer perceptron model`.
- The output of one perceptron are  directly fed into as inputs to another perceptron.
- This allows the network as a whole to learn about interactions and relationships between features.
- The first layer is the input layer.
- The last layer is the output layer.
- Layers in between are hidden layers.
- Neural networks become `deep neural networks` if they contain 2 or more hidden layers.

### Universal Approximation Theorem

## Activation Functions

- Used to set boundaries to output values from the neuron.

### Multi-Class Activation Functions

#### Multi-Class Situations

- Non-Exclusive Class
    - A data point can have multiple classes/categories assigned to it
    - Photos can have multiple tags (eg: beach, family, vacation etc)
- Mutually Exclusive Classes
    - Only one class per data point
    - Photos can be colorful or grayscale
    - The range will be 0 to 1, and the sum of all the probabilities will be equal to one.
    - The model returns the probabilities of each class and the target class chosen will have the highest probability.

## Gradient Descent

## Cost Functions

## Feed Forward Functions

## BackPropagation



