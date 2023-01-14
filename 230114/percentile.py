#!/usr/bin/python3

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import sys

NUM_TRIAL = 2000

def calcPlotData(numSamplings, percentiles, dist):
    plotXData = np.array([])
    plotYData = np.array([])
    for percentile in percentiles:
        tmpPlotXData = np.array([])
        tmpPlotYData = np.array([])
        for numSampling in numSamplings:
            scores = calcScoresAtPercentile(numSampling, percentile, dist) 
            tmpPlotXData = np.append(tmpPlotXData, numSampling)
            tmpPlotYData = np.append(tmpPlotYData, np.std(scores, ddof=1))
        plotXData = np.append(plotXData, tmpPlotXData)
        plotYData = np.append(plotYData, tmpPlotYData)

    return plotXData.reshape(len(percentiles), len(numSamplings)), plotYData.reshape(len(percentiles), len(numSamplings))

def calcScoresAtPercentile(numSampling, percentile, dist):
    scoresAtPercentile = np.array([])
    for i in range(NUM_TRIAL):
        samples = dist.rvs(size=numSampling)
        scoresAtPercentile = np.append(scoresAtPercentile, stats.scoreatpercentile(samples, percentile))

    return scoresAtPercentile

def plot(title, plotXData, plotYData, percentiles):
    plt.clf()
    plt.figure(figsize=(15, 9))
    plt.rcParams["font.size"] = 24
    plt.xticks(np.arange(0, np.max(plotXData)+10, 10))
    plt.grid()
    for i, x in enumerate(plotXData):
        plt.plot(x, plotYData[i], marker='o', label='percentile='+str(percentiles[i]))
    plt.title(title)
    plt.xlabel("The number of samples")
    plt.ylabel("Standard deviation")
    plt.legend()
    plt.savefig(title.replace(" ", "_").lower() + ".png", dpi=200)

def main():
    numSamplings = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    percentiles = [1, 10, 50, 90, 99]
    dists = {
        "Uniform distribution": stats.uniform(),
        "Normal distribution": stats.norm(),
        "Exponential distribution": stats.expon()
    }
    for distName, dist in dists.items():
        print("dist: {}".format(distName))
        plotXData, plotYData = calcPlotData(numSamplings, percentiles, dist)
        plot(distName, plotXData, plotYData, percentiles)

if __name__ == "__main__":
    main()

