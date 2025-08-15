## Import all the required libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# read the data in csv file 
data = pd.read_csv(r"C:\Desktop\Data-Science-Cohort\Phase-1\Population_Survey_Data_lyst1750274390196.csv")
print(data.head())
print(data.shape)

# Simple Random Sampling : 100 Records Randomly 

sample_data = data.sample(n=100, random_state=44)
print(sample_data)

# Stratified Random Sampling

Stratified_Random_data = data.groupby('Region').apply(lambda x : x.sample(min(len(x), 25), random_state=44))
print(Stratified_Random_data)

#  Cluster Sampling : Manufacturing Data by Batch Number
data = pd.read_csv(r"Phase-1/Manufacturing_Data_lyst1750274395200.csv")
cluster = data['BatchNumber'].unique()
print(cluster)

Selected_cluster = np.random.choice(cluster, size=5, replace=False)
print(Selected_cluster)

clustered_sample = data[data['BatchNumber'].isin(Selected_cluster)]
print(clustered_sample)

# Systemtic sampling
systemtic_sample  = data.iloc[::10, :]
print(systemtic_sample)