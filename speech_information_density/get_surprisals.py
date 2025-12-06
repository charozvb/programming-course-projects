from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys, time

def get_lines(path):
    #takes a file path and returns the lines in the file as a list of strings
    with open(path, "r") as f:
        lines = f.read()
    return lines

def get_unigrams(lst_sentences):
    #takes a list of strings, returns a dict with unigrams and their frequencies
    d_unigram = defaultdict(lambda: 1)
    for sentence in lst_sentences:
        d_unigram['<s>'] += 1
        d_unigram['<e>'] += 1
        for words in word_tokenize(sentence):
            d_unigram[words] += 1
    return d_unigram

def get_bigrams(lst_sentences):
    #takes a list of strings, returns a dict with bigrams and their frequencies
    d_bigram = defaultdict(lambda: 1)
    for sentence in lst_sentences:
        sentence = word_tokenize(sentence)
        d_bigram[('<s>', sentence[0].lower())] += 1
        d_bigram[(sentence[-1], '<e>')] += 1
        for words in range(1, len(sentence)-1):
            bigram = sentence[words].lower(), sentence[words+1].lower()
            d_bigram[bigram] += 1
    return d_bigram

def get_surprisal(p):
    #takes a probability, returns the surprisal
    surprisal = - (log(p, 2))
    return surprisal

def get_bigram_surprisal(d_unigram, d_bigram):
    #takes 2 dicts (unigrams+bigrams), returns another dict with bigrams and their surprisal values using get_surprisal()
    frequency = []
    d_surprisal = defaultdict(int)
    for unigram in d_unigram:
        for bigram in d_bigram:
            if bigram[0] == unigram:
                frequency = d_unigram.get(unigram)
                conditionalprob = ((d_bigram[bigram] + 1) / (frequency + len(d_unigram)))
                surprisal = get_surprisal(conditionalprob)
                d_surprisal[bigram] = surprisal
    return d_surprisal

def get_test_surprisal(sentence, d_bigram, d_unigram):
    #takes a sentence, returns the average surprisal of that sentence(unless you go for the word level)
    average_surprisal = []
    for i in range(len(sentence)-1):
            p = d_bigram[(sentence[i], sentence[i+1])] / d_unigram[sentence[i]]
            surprisal = - (log(p, 2))
            average_surprisal.append(surprisal)
    average = (sum(average_surprisal) / len(average_surprisal))
    return average
    

if __name__ == "__main__":
    train_data = get_lines(sys.argv[1])
    train_string = " ".join(train_data)
    train = sent_tokenize(train_string)
    sentence = get_lines(sys.argv[2])
    sentence_string = " ".join(sentence)
    tokenized = word_tokenize(sentence_string)
    tokenized = [word.lower() for word in tokenized]

    #print unigram:
    unigram_freq = get_unigrams(train)

    #print bigram:
    bigram_freq = get_bigrams(train)

    #print surprisal:

    #print test surprisal:
    test_surprisal = get_test_surprisal(tokenized, bigram_freq, unigram_freq)
    print(test_surprisal)




