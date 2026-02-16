from datsci_testing.readers import har
from datsci_testing import reusable_classifier
import pandas as pd
import numpy as np
import os
import random
import sklearn

"""
Predicts sleeping status of an individual using step count.
Examines how effective this is at predicting sleeping status.
"""


#Initialize the data frame we'll work with and other important variables
path=os.path.join("data","motion-and-heart-rate-from-a-wrist-worn-wearable-and-labeled-sleep-from-polysomnography-1.0.0")
har_dat=har.HAR(path,10)
#working dataframe
hdf=har_dat.df.copy()
#get absolute values of acceleration
hdf['acc_x']=hdf['acc_x'].abs()
hdf['acc_y']=hdf['acc_y'].abs()
hdf['acc_z']=hdf['acc_z'].abs()
#turn time into seconds
hdf.index=pd.to_timedelta(hdf["timestamp"], unit="s")

# We need to loop through peopel so that we don't average across them
people = pd.unique(hdf["person"])
features, labels, test_features, test_labels = [], [], [], []
for person in people:
    print(f"Computing person {person+1}")
    df = hdf.loc[hdf["person"] == person]
    # Compute a whole bunch of window/column features
    for window in ["10s", "1min", "10min", "1h", "10h"]:
        for column in ["hr", "acc_x", "acc_y", "acc_z"]:
            for fn in ["mean", "min", "max", "std"]:
                df[f"{column}_{fn}_{window}"] = df[column].rolling(window).agg(fn)

    # Then downsample the data. The lowest frequency we care about is 10s
    df = df.resample("10s").first().dropna(how="any")

    # Extract features, labels, and classify
    fs = df.drop(columns=["timestamp", "hr", "acc_x", "acc_y", "acc_z", "is_sleep"])
    ls = df["is_sleep"]

    #divide into test and not test randomly
    if random.randint(0,1) < 0.5:
        test_features.append(fs)
        test_labels.append(ls)
    else:
        features.append(fs)
        labels.append(ls)

#random forest model
classifier = reusable_classifier.ReusableClassifier("random_forest")
classifier.train(pd.concat(features), pd.concat(labels))

pred_labels = classifier.predict(pd.concat(test_features))
test_labels = pd.concat(test_labels)

count_equal = (pred_labels.astype(int) == test_labels.to_numpy().astype(int)).sum()
print(count_equal / len(test_labels))

#xgboost model
classifier2 = reusable_classifier.ReusableClassifier("xgboost")
classifier2.train(pd.concat(features), pd.concat(labels))
pred_labels = classifier2.predict(pd.concat(test_features))
count_equal = (pred_labels.astype(int) == test_labels.to_numpy().astype(int)).sum()
print(count_equal / len(test_labels))