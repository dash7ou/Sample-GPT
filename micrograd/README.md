# Micrograd: A Minimalistic Neural Network Library

Micrograd is a compact, self-contained library that implements a simple automatic differentiation (autograd) engine and a neural network library on top of it, inspired by PyTorch. It is designed for educational purposes, providing a clear and concise implementation of backpropagation and neural network components. The library operates over scalar values, constructing dynamic computation graphs to perform reverse-mode automatic differentiation.

## Core Components

The library is organized into two main modules:

1. **Engine:** Contains the foundational `Value` class, which enables the construction of computation graphs and automatic differentiation.
2. **Neural Network** : Builds upon the engine to provide classes for constructing neural networks, including `Neuron`, `Layer`, and `MLP`.

### Engine Module

#### `Value` Class

The `Value` class represents a single scalar value in the computation graph. Each `Value` object stores:

* `data`: The scalar value.
* `grad`: The gradient of the value with respect to some scalar quantity (initialized to 0).
* `_backward`: A function to compute the gradient of the value.
* `_prev`: A set containing parent `Value` objects in the computation graph.
* `_op`: The operation that produced this `Value` (for visualization purposes).

The class supports basic arithmetic operations (`+`, `-`, `*`, `/`, `**`) and includes methods for activation functions like `tanh` and `relu`. The `backward` method performs a reverse-mode automatic differentiation to compute gradients for all `Value` objects in the graph.

### Neural Network Module

#### `Module` Class

An abstract base class representing a neural network module. It provides two methods:

* `zero_grad()`: Sets the gradients of all parameters to zero.
* `parameters()`: Returns a list of parameters involved in the module.

#### `Neuron` Class

Represents a single neuron in the network. Each neuron has:

* `w`: A list of weights (`Value` objects) initialized randomly.
* `b`: A bias term (`Value` object) initialized to zero.
* `nonlin`: A boolean indicating whether to apply a non-linear activation function (ReLU).

The `__call__` method computes the neuron's output by performing a weighted sum of the inputs and adding the bias. If `nonlin` is `True`, the ReLU activation function is applied.

#### `Layer` Class

Represents a layer of neurons. Each layer contains:

* `neurons`: A list of `Neuron` objects.

The `__call__` method applies each neuron to the input and returns the list of outputs. The `parameters` method aggregates the parameters from all neurons in the layer.

#### `MLP` Class

Represents a multi-layer perceptron (MLP), which is a simple neural network composed of multiple layers. The `MLP` class has:

* `layers`: A list of `Layer` objects.

The `__call__` method processes the input through each layer sequentially, returning the final output. The `parameters` method aggregates parameters from all layers.

## Example Usage

Here's an example of how to create and train a simple neural network using Micrograd:

```python


# Initialize a 2-layer MLP with 3 input features and two hidden layers of 4 and 4 neurons
model = MLP(3, [4, 4, 1])

# Example input
x = [Value(1.0), Value(-2.0), Value(3.0)]

# Forward pass
output = model(x)

# Compute loss (assuming some target value)
target = Value(1.0)
loss = (output - target) ** 2

# Backward pass
model.zero_grad()
loss.backward()

# Update parameters (simple gradient descent)
learning_rate = 0.01
for p in model.parameters():
    p.data -= learning_rate * p.grad
```

This example demonstrates the creation of a simple MLP, performing a forward pass to compute the output, calculating a loss, performing backpropagation to compute gradients, and updating the model parameters using gradient descent.

## Conclusion

Micrograd provides a minimalistic and transparent implementation of an autograd engine and neural network components, making it an excellent resource for learning and experimenting with the fundamentals of neural network training and backpropagation.
