import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
#importing the functions from get_durations.py and get_surprisals.yp that i will need to create the data.csv file. I need the csv_files and the get_durations function to read the durations; and the get_test_surprisal function and the sentences (in the txt file) to calculate the surprisals
from get_surprisals import get_test_surprisal, get_unigrams, get_bigrams
from get_durations import get_durations
from get_durations import get_lines


def safe_get_lines(path):
    #to catch UnicodeCodeErrors and FileNotFoundErrors when trying to create the data.csv file
    try:
        with open(path, "r", encoding="utf-8") as f:
            #if the file is utf-8, it returns the line and removes the last \n characters
            return [line.strip() for line in f.readlines()]
    except UnicodeDecodeError:
        with open(path, "r", encoding="cp1252") as f:
            #if line is not utf-8, encodes with cp1252
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        #if the file doesnt exist, prints a message and returns an empty list:
        print(f"File not found: {path}")
        return []


def get_data(csv_files, sentences):
    data = []
    d_unigram = get_unigrams(sentences)
    d_bigram = get_bigrams(sentences)
    for i in range(len(csv_files)):
        #reading the durations
        lines = get_lines(csv_files[i])
        duration = get_durations(lines)
        #summing durations for the whole sentence
        sentence_duration = sum(duration.values())

        #calculate surprisal:
        surprisal = get_test_surprisal(sentences[i], d_bigram, d_unigram)
        #create a list for each pair of duration and surprisal (for each sentence)
        row = [sentence_duration, surprisal]
        #append the lists into a bigger list:
        data.append(row)
        #create the csv file using pandas:
    df = pd.DataFrame(data, columns=["duration", "surprisal"])
    df.to_csv("data.csv", index=False)
    return df


def get_linear(path, x_par, y_par):
   df = pd.read_csv(path)

   df[y_par] = np.log(df[y_par])
   sns.regplot(
           data=df, x=x_par, y=y_par,
           scatter_kws={"s":10},
           line_kws={"color":"blue", "linewidth": 0.8})
   plt.xlabel(f"Log({x_par})")
   plt.ylabel(f"Log({y_par})")
   plt.savefig("log_reg_plot.png")
   slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])
   intercept_original = np.exp(intercept)
   slope_original = np.exp(slope)
   return {
           "Intercept": intercept_original,
           "Coefficient": slope_original,
           "R-squared": r_value**2,
           "p-value": p_value
            }

def main():
    #printing out the lines to create the csv file so it doesnt get created each time i run the code:
    #csv_files_lst = safe_get_lines(sys.argv[1])
    #sentences_lst = safe_get_lines(sys.argv[2])
    #df = get_data(csv_files_lst, sentences_lst)
    #print with ("data.csv", surprisal, duration):
    regression = get_linear("data.csv", "surprisal", "duration")
    print(regression)
main()
