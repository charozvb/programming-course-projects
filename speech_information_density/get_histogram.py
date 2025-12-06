import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def get_histogram(path):
    #outputs a histogram of the duration on the x-axis and their frequencies on the y-axis
    df= pd.read_csv(path)
    #pass the correct column of data.csv to seaborn:
    sns.histplot(df["duration"], color="blue")
    #adding labels:
    plt.xlabel("Duration")
    plt.ylabel("Frequency of duration")
    plt.savefig("duration_histogram.png")


def main():
    path = "data.csv"
    get_histogram(path)

main()

