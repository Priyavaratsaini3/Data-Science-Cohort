## 1. Evaluate the measure of central tendency for the whole data followed by the simple random sample , stratified random sample , cluster sample and systematic sample.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt 

data = pd.read_csv(r'Phase-1\Population_Survey_Data_lyst1750274390196.csv')

## Simple Random Sample to Measure of the Central Tendency 
newdata = data['Income']

simple_randomSample = newdata.sample(n=100 , random_state=44)

mean_value = np.mean(simple_randomSample)
print("mean of the Simple Random Sample", mean_value)

median_value = np.median(simple_randomSample)
print("median of the Simple Random Sample",median_value)

mode_value = stats.mode(simple_randomSample, keepdims=True)
print("mode of the Simple Random Sample",mode_value.mode[0])

print("--------------------------------------------------------------------------------------------")

##Stratified Random Sample to Measure of the Central Tendency 

stratified_random_sampling = data.groupby('Region').apply(lambda x : x.sample(min(len(x), 25 ), random_state= 44))
new_stratified = stratified_random_sampling['Income']

mean_of_stratified = np.mean(new_stratified)
print("mean of the Stratified Random Sample --> ", mean_of_stratified)

median_of_stratified = np.median(new_stratified)
print("median of the Stratified Random Sample --> ",median_of_stratified)

mode_of_stratified = stats.mode(new_stratified, keepdims=True)
print("mode of the Stratified Random Sample --> ",mode_of_stratified.mode[0])

print("--------------------------------------------------------------------------------------------")
## Cluster Random Sample to Measure of the Central Tendency 

Cluster_random_sampling = data['Region'].sample(n=1, random_state=44).iloc[0]

cluster_sample = data[data['Region'] == Cluster_random_sampling]['Income'] 

mean_of_cluster = np.mean(cluster_sample)
print("mean of the Cluster Random Sample -->", mean_of_cluster)

median_of_cluster = np.median(cluster_sample)
print("median of the Cluster Random Sample -->",median_of_cluster)

mode_of_cluster = stats.mode(cluster_sample, keepdims=True)
print("mode of the Cluster Random Sample -->",mode_of_cluster.mode[0])

print("--------------------------------------------------------------------------------------------")

## Systemtic Random Sample to Measure of the Central Tendency 

Systemtic_Sampling = data['Income'].iloc[::10]

mean_of_systemtic = np.mean(Systemtic_Sampling)
print("mean of the Systemtic Random Sample -->", mean_of_systemtic)

median_of_systemtic = np.median(Systemtic_Sampling)
print("median of the Systemtic Random Sample -->",median_of_systemtic)

mode_of_systemtic = stats.mode(Systemtic_Sampling, keepdims=True)
print("mode of the Systemtic Random Sample -->",mode_of_systemtic.mode[0])

print("--------------------------------------------------------------------------------------------")

## Mean of the population 
## 3. Finally, conclude which specific sampling technique mean value is almost similar to the population mean value. 

population_mean = np.mean(newdata) 
print("mean of the Population Data -->", population_mean)

# Bar plot of the all samples means 
plt.figure(figsize=(10,6))
methods = ["Simple Random", "Stratified", "Cluster", "Systematic"]
means = [mean_value, mean_of_stratified, mean_of_cluster, mean_of_systemtic]
plt.bar(methods, means, color="skyblue")
plt.axhline(np.mean(newdata), color="red", linestyle="--", label="Population Mean")
plt.title("Comparison of Means of Different Samples")
plt.xlabel("Sampling Method")
plt.ylabel("Mean Income")
plt.legend()
plt.show()



