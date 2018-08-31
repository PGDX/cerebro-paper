#!/usr/bin/env python

# Copyright 2017, Personal Genome Diagnostics.

import numpy as np
from sklearn import ensemble
from sklearn import metrics
from sklearn.externals import joblib
import sys

data_file = sys.argv[1]
model_dir = sys.argv[2]

data = []
with open(data_file) as f:
  for line in f:
    fields = line.strip().split("\t")
    features = [ float(feature) for feature in fields[2:] ]
    # first two features: SBS? INS? (DEL is 0/0)
    if fields[1] == "INS":
      features = [ 0 ] + features
    else:
      features = [ 1 ] + features
    if fields[1] == "SBS":
      features = [ 0 ] + features
    else:
      features = [ 1 ] + features
    data.append(features)

print "Done reading"

variants = []
truth = []
np.random.shuffle(data)
false_count = 0
true_count = 0
for point in data:
  if point.pop() == 0:
    variants.append(point)
    truth.append(0.0)
    false_count += 1
  else:
    variants.append(point)
    truth.append(1.0)
    true_count += 1

print "False points: " + str(false_count)
print "True points: " + str(true_count)

X_train = np.array(variants)
y_train = np.array(truth)

print "Done converting"

model = ensemble.ExtraTreesClassifier(n_estimators=1000, n_jobs=-1)
model.fit(X_train, y_train)
print "Done fitting"

model.set_params(n_jobs=1)
joblib.dump(model, model_dir + '/cerebro.model')
