# Interconnect Neural Network
This project aims to design a neural network capable of creating interconnections between logical modules of varying complexity, in any language. Initial focus will be on Boolean operators and hardware description languages.

A best-case outcome is to have the project generate accurate graphs from data. This graph would then be translated by another program into a useful or readable format (source code or a netlist).

The current plan is to embed layers with the lowest-level language structures required for a use case, then iterate on the case's data to expand the vocabulary supported by the network, in order to allow support for operator inheritance (if needed). 

# Process
1. Given some input data set, e.g. a dataset of binary strings, structure the network to use only binary weights (simplifying computation).
  a. Make each layer connect with a general-purpose module (a Docker container).
  b. Have a 1-1 map between layer weights and each item in the container (this module could be a list of every item in a language that introduces a change in program/circuit state)

2. Start with binary strings and Boolean operators.

3. Test ability of the network to interconnect arbitrarily complex modules (e.g. pack two complex and interdependent circuit graphs into separate containers, along with all operators that were initially needed to form them, then see if the new graph figured out that it was best to interconnect them). If successful, this will form a basis for a module inheritance process.

# Notes
1. TensorFlow Lanbda function issue: tf.Lambda operators don't work in a neural net when they contain steps up or down in dimension. Unsuitable for use in operators that need dimensionality steps.
2. Check viability for TensorFlow GPU acceleration (use in tf operator) of Python-wrapped libraries designed to interface with low-level languages (Xilinx Vivado, Cython, etc.)
3. If TensorFlow Operators don't work, look at using Docker containers for custom language runtimes (very slow - options for GPU acceleration?).
4. Include 'pass' operator in every layer (removes need for layer 1 to be densely connected to layer 6).
5. Should data inheritance/storage modules be included by default?

# Do List
- Build Docker containers
- Make Tensorflow graph
- Make sample data (Random binary inputs -> composition of logic gates)
