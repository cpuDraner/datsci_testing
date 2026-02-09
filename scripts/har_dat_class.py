from datsci_testing.readers import har
from datsci_testing import reusable_classifier
import pandas as pd
import numpy as np

"""
Predicts sleeping status of an individual using step count.
Examines how effective this is at predicting sleeping status.
"""

"""
Initialize the data frame we'll work with and other important variables
"""
har_dat=har.HAR(
    "data\motion-and-heart-rate-from-a-wrist-worn-wearable-and-labeled-sleep-from-polysomnography-1.0.0.zip", 
    10)
#working dataframe
hdf=har_dat.df.copy()

#change the index to be in seconds
hdf.index=pd.to_timedelta(hdf['timestamp'], unit='s')

#get training data into a timeframe that works for us
hdf=hdf.resample('60s').first().dropna()

#create a list of the features and labels

print(f"Correct: {correct}/{total}")
print(f"Accuracy: {correct/total}")