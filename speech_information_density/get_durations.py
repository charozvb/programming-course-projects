from collections import defaultdict
import sys

def get_lines(path):
    #takes a path to a file
    # returns those lines in a list of strings
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def get_durations(lst_strings):
    #takes a list of strings where each string is a line in a file
    #returns a dict whose keys are orthographic words and values the words durations in milliseconds
    id_durations = defaultdict(list)
    for sentence in lst_strings[1:]:
        columns = sentence.split(";")
        word = columns[5]
        duration_value = float(columns[1])
        id_durations[word].append(duration_value)
    for word in id_durations:
        #convert durations into ms:
        durations_in_ms = [(d / 48000) * 1000 for d in id_durations[word]]
        id_durations[word] = sum(durations_in_ms)
    return id_durations

if __name__ == "__main__":
    #read lines of file:
    csv_file = get_lines(sys.argv[1])
    durations = get_durations(csv_file)
    print(durations)



