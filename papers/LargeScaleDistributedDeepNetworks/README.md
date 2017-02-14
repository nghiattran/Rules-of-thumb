# Large Scale Distributed Deep Network

# 1. Introduction

Two novel methods for large-scale distributed training: 

1. Downpour SGD, an asynchronous stochastic gradient descent procedure which leverages adaptive learning rates and supports a large number of model replicas, and 
2. Sandblaster L-BFGS, a distributed implementation of [L-BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS) that uses both data and model parallelism. 

Both Downpour SGD and Sandblaster L-BFGS enjoy significant speed gains compared to more conventional implementations of SGD and L-BFGS.

