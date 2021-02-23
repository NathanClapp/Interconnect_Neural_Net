# Interconnect Neural Network
This project aims to design a neural network capable of creating interconnections between logical modules of varying complexity. Initial focus will be on Boolean operators and hardware description languages.

A best-case outcome is to produce a network layer defined with a Docker (or some lighter-weight container) interface, capable of interfacing with Tensorflow/Keras networks and able to pipe data from one container to another, as dictated by layer weights.

Combined with graph searching algorithms, a project-specific interpreter, and a repackaging script, this project would become capable of generating source code based on specific use case requirements, as well as repackaging contents of previous container generations into new container generations (allowing code encapsulation). Kubernetes may become useful for load balancing containers during network runtime.

### Process
Given some input data set, e.g. a dataset of binary strings, initialize a feedforward network composed of Docker-embedded layers to use only 1-bit weights. (This may slightly simplify computation, but more importantly would provide both an adjacency tensor and elimination of arbitrary transformations within the portion of the layer containing weights.)

#### Dense Container-Embedded Layer Architecture
  - Make each layer connect with a general-purpose module (a Docker container).
      - Via networking; UDP may be best due to its light weight.
  - Map tensor elements (post dot operation) to set of all inputs for functions in the container on a 1-1 basis.
  - Return function outputs or errors. Discard or print errors, but return the original input data with the rest of the processed data if an error takes place.
  - Encode returns such that an activation function is still useful, while preserving return values.
  - Pass data back to Tensorflow.
  - Apply activation function.

#### Testing
Test ability of the network to interconnect arbitrarily complex modules (e.g. pack two complex and interdependent circuit graphs into separate containers, along with all operators that were initially needed to form them, then see if the new graph figured out that it was best to interconnect the complex modules and not their basic components). If successful, this will form a basis for a module inheritance process.

### Notes
- tf.Lambda doesn't appear to work in a neural net when functions contain steps up or down in dimension. Unsuitable for complex operations requiring I/O asymmmetry.
- tf.map_fn does have support for I/O asymmetry, but does not support arbitrary runtimes.
- This project will be very CPU-heavy when scaling complexity of individual containers. When parsing trained graphs into code, focus especially on loading to FPGA.
- Need for 'pass' operator in every layer? (removes need for layer 1 to be densely connected to layer 6, but would need an extra container ).
- Storage modules? (docker volumes, bind mounts as a last resort)
- Project may be incompatible with graph compilation - requires eager execution at present due to UDP client/possibly communication with Docker.
- Dependencies:
    - Python 3.8.5 64-bit
      - socket, os, sys, json, inspect
    - Tensorflow 2.3.1
    - GNU programs:
      - mkfifo, parallel
    - Docker
      - tbd
    - Kubernetes?

### Do List
##### Small/Fast Checkpoints
- Build Docker containers
- Make Tensorflow graph
- Find suitable activation(s)
- Generate sample data (All combinations of binary inputs -> composition of logic gates)

##### Large/Slow Checkpoints
- Replace all UDP server and container-side stuff with faster Go implementations (after proof of concept stuff works)
 - Look into replacing Python UDP client (layer-side) with Go version. Import as a module? Is this needed at all?
- Define standards or guidelines for:
 - Layer/Docker interfaces
 - Docker/code module packaging
  -stdio and stderr interface with code modules
- Expand embedding to more layer types - recurrent, LSTM, maybe convolutional?
