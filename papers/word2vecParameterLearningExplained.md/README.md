# word2vec Parameter Learning Explained

## 1 Continuous Bag-of-Word Model

### 1.1 One-word context

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

### 1.2 Multi-word context

Example of a Multi-word CBOW model:
![Multi-word CBOW](CBOW_multi_word.png)

So the hidden layer is computed as:

<strong>h = W<sup>T</sup>(x<sub>1</sub> + x<sub>2</sub> + ... + x<sub>C</sub>) / C</strong>

## 2 Skip-Gram Model

In this model, the hidden layer behaves as a lookup table just like in one-word context CBOW

[Souce](http://www-personal.umich.edu/~ronxin/pdf/w2vexp.pdf)