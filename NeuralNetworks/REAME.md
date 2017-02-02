# Neural Networks

## 1. Word2Vec

### 1.1 Introduction

In a sense, Word2Vec tries to map human words to a vector space in which related or requently used words are located near to each other. A group of nearby or related words can be called a **Bag of Words**.

TODO: come back and check **bag-of-word** (CBOW) vs **skip-gram** (SG) models

#### Word2Vec features

TODO: This section is personal perception

Bags of words are useful in predicting the next word in a setence. For example, image you are given a short phrase, "United States ___ America", a normal human being would be able to fill in the blank relatively easy. As a human, we look at nearby words of the missing and do a quick prediction.  

Word2Vec is relatively similar to above perspective. It also looks at nearby words, which is words that are in its **window size** hyperparameter, to group words together.

For example, a Word2Vec system can form a bag of words of "cat", "kitten", "dog", and "puppy" because they are all dosmestic animals.  

### 1.2 Terminologies

**Window size**: defines number of nearby words on one side of the word in a con text.

![Window](window.png)

**Input**: a one-hot `n`-dimensional vector where `n` is the number of unique words. So, each input represents a word.

**Output**: a one-hot `n`-dimensional vector in training stage becaue we need  it to only represent a single word. But when evaluate the trained network the output will actually be a probability distribution vector which show all possible words, not just one.

Since the ouput is a `n`-dimensional vector for every iteration, the number of possible output sequence grows exponentially. To prevent this growth, we use a technique called **pruning** to eliminate majority of words and only keep ones high probability.

### 1.3 Skip Gram

For example, we tries to design and 2-layers skip gram model with `N` neurons in the hidden layers to map a text with a dictionary of size `V`

### 1.3.1 The Hidden Layer

Since we have `v` neurons in the input layer and `h` in the hidden, the weight matrix size between these two is `N`x`V`. Assume the network gets an input `x` as x<sub>k</sub> = 1 and x<sub>k'</sub> = 0 for k != k', we have:

<strong>h = xW = W(k,·)</strong>

Which technically copies a row of the weight matrix and uses it as activations for the hidden layer. So, the hidden layer acts as a lookup table. It sort of maps the original `V`-dimensional plane to a context `N`-dimentional plane to feed in the the output layer. Think of it as a word with no context and a word with context.

![Lookup table](lookup_table.png)

### 1.3.2 The Output Layer

The output layer for Skip Gram model is similar to normal neural network.

<strong>o = hW</strong>

## 1.4 Continuous Bag-of-Word Model

### 1.4.1 One-word context

Our assuption for this study is that the network only predicts one target word for each given context word.

Example of a CBOW model:
![Single-word CBOW](CBOW_single_word.png)

Where:
* `V`: size of the dictionary (number of unique words).
* `x`: `V`-dimentional input vector. x<sub>i</sub> value of `x` and i<sup>th</sup> position. The input is a one-hot encoded vector.
* `h`: `N`-dimensional vector represent neurons in hidden layer.
* `y`: `V`-dimentional output vector.
* `W`, `W'`: weights between layers. 

Denote row `i` of W as <strong>v<sub>w</sub><sup>T</sup></strong>. Assume the network gets an input `x` as x<sub>k</sub> = 1 and x<sub>k'</sub> = 0 for k != k', we have

<strong>h = W<sup>T</sup>x = W<sup>T</sup><sub>(k,·)</sub> := v<sup>T</sup><sub>wI</sub></strong>

NOTE: some sections left out

### 1.4.2 Multi-word context

Example of a Multi-word CBOW model:
![Multi-word CBOW](CBOW_multi_word.png)

So the hidden layer is computed as:

<strong>h = W<sup>T</sup>(x<sub>1</sub> + x<sub>2</sub> + ... + x<sub>C</sub>) / C</strong>

## 2. Recurrent Neural Networks (RNNs)

One problem with vanilla neural nets and convolution neural nets is that they are fixed in term of input size, output size, and computational steps. For these types of network, for each input, a network will only produce one output which is undesirable in many fields such as Naural Language Processing (NPL). In NLP, one input usually requires multiple output values. For example, consider a word is a one hot N-dimensional vecor where N is the number of unique word in the entire dictionary.



## 3. Long Short Term Memorys (LSTMs)

TODO

## 4 Update functions

### 4.1 Gradient descent

<strong>v = - learning_rate * d<sub>x</sub></strong>

### 4.2 Momentum update

Momentum kind of shoots ahead by using big update steps. Sometimes it overshoots and overall much better than vanila GD 

<strong>v = mu * v - learning_rate * d<sub>x</sub></strong>

### 4.3 Nesterov Momentum update (Nesterov Accelerated Gradient, nag)

<strong>v_prev = v</strong>
<strong>v = mu * v - learning_rate * d<sub>x</sub></strong>
<strong>v = -mu * v_prev + (1 + mu) * v</strong>

### 4.4 AdaGrad update

<strong>cache += d<sub>x</sub></strong>
<strong>v = mu * v - learning_rate * d<sub>x</sub></strong>

[word2vec Parameter Learning Explained](http://www-personal.umich.edu/~ronxin/pdf/w2vexp.pdf)

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
