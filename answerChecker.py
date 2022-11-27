# THIS IS A SIMPLE STATISTIC QUESTION ANSWER CHECKER PROGRAM
# THIS PROGRAM CAN LET USER INPUT A DATA SET AND AUTOMATIC CALCULATE
# MEAN,MEDIAN,POPULATION STANDARD DEVIATION,SAMPLE STANDARD DEVIATION,POPULATION VARIANCE,SAMPLE VARIANCE,INTERQUATILE RANGE AND RANGE
# THIS PROGRAM NOT INCLUDE AUTO-DRAW GRAPH YET
# THIS PROGRAM ONLY CAN PROCESS WITH UNGROUPED DATA

import statistics
import numpy
from scipy.stats import skew
# import matplotlib.pyplot as plt

dataList = []

numberData = int(input("Number of Data : "))

for x in range(0,numberData):
    data = float(input("Data " + str(x + 1) + " : "))
    dataList.append(data)

mean = statistics.mean(dataList)
median = statistics.median(dataList)
populationStd = statistics.pstdev(dataList)
sampleStd = statistics.stdev(dataList)
populationVarc = statistics.pvariance(dataList)
sampleVarc = statistics.variance(dataList)

q3,q1 = numpy.percentile(dataList,[75,25])
interquartileRange = q3 - q1

dataRange = max(dataList) - min(dataList)

# Skewness is not comform either the question demand adjusted or unadjusted skewness
# Default == (bias=true) -> unadjusted
skewness = skew(dataList)

print(" ")
print("Data List : " ,dataList)
print(" ")

answer = ("Mean : {:.4f}\nMedian : {}\nPopulation Std : {:.4f}\nSample Std : {:.4f}\nPopulation Varc : {:.4f}\nSample Varc : {:.4f}\nInterquartile Range : {:.4f}\nRange : {:.4f}\nSkewness : {:.4f}\n")

print(answer.format(mean,median,populationStd,sampleStd,populationVarc,sampleVarc,interquartileRange,dataRange,skewness))

# plt.hist(dataList)
# plt.show()
