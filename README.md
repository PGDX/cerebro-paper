# Cerebro

> Cerebro is a machine-learning classifier for somatic mutation detection based on an extremely randomized trees model. 

>This package includes two scripts for training and executing the 
Cerebro model for somatic mutation identification from whole-
exome next-generation sequencing data.  Required input is a set of candidate variants and informative features as described below.

## Requirements 
This code requires the following dependencies
* Python (v2.7) https://www.python.org/
* numpy (v1.8) http://www.numpy.org/
* scikit-learn (0.19.1) http://scikit-learn.org/stable/index.html

## Training and Testing Datasets

Training data must consist of tab-delimited integers or decimal values, with the exception of the first two columns which are formatted as:
* a unique identifier per mutation candidate
* the mutation type (SBS/INS/DEL)
* a final column consisting of either 0 (for known incorrect calls) or 1 for true somatic mutations

See the file *example_points.txt* for an example.

Testing data follows the same format as the training data, but without the final column of 0s and 1s.

----
## Usage
To train the model, execute the command:

    mkdir trained_model && ./cerebro_train.py example_points.txt trained_model

To run the trained model on new data, execute the command

    ./cerebro_call.py testing_points.txt trained_model > classifications.txt


README documentation

2017-12-15 -- Source code and example training data for Cerebro
somatic mutation confidence scoring.

This package includes two scripts for training and executing the 
Cerebro model for somatic mutation identification from whole-
exome next-generation sequencing data.  Required input is a set of
candidate variants and informative features.

Training Data Example (example_points.txt)
This data must consist of tab-delimited integers or decimal values, 
with the exception of the first two columns which are formatted as:
1. a unique identifier per mutation candidate
2. the mutation type (SBS/INS/DEL)

The final column must consist of either 0 (for incorrect calls) or 
1 for true somatic mutations.

To train the model, execute the command:
mkdir trained_model && ./cerebro_train.py example_points.txt trained_model

To run the trained model on new data, execute the command
./cerebro_call.py testing_points.txt trained_model

