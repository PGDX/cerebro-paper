#!/usr/bin/env python

# Copyright 2017, Personal Genome Diagnostics.

import numpy as np
from sklearn import ensemble
from sklearn import metrics
from sklearn.externals import joblib
import sys

data_file = sys.argv[1]
model_dir = sys.argv[2]
model = joblib.load(model_dir + '/cerebro.model')

def print_results(cuids, data):
  X_test = np.array(data)
  y_pred = model.predict_proba(X_test)
  for num in y_pred:
    print cuids[0] + "\t" + str(num[1])
    del cuids[0]

data = []
cuids = []
with open(data_file) as f:
  for line in f:
    fields = line.strip().split("\t")
    features = [ float(feature) for feature in fields[2:] ]
    if fields[1] == "INS":
      features = [ 0 ] + features
    else:
      features = [ 1 ] + features
    if fields[1] == "SBS":
      features = [ 0 ] + features
    else:
      features = [ 1 ] + features
    data.append(features)
    cuids.append(fields[0])
    if len(data) == 10000:
      print_results(cuids, data)
      cuids = []
      data = []
if len(data) != 0:
  print_results(cuids, data)
