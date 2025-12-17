
from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
import sys
import random



def read_lexicon(path):
    #read the lexicon and returns a set of strings
    with open(path, "r") as f:
        word_set = f.readlines()
        word_set = [x.strip() for x in word_set]
        return set(word_set)

class AutoCorrect:
    #has a constructor and 5 methods
    def __init__(self, word_list, alpha):
        #takes 2 arguments besides self: word_list and alpha
        self.word_list = word_list
        # word_list = set of words
        self.alpha = alpha
        # alpha = english alphabet as a string
        

    def insertion(self, word):
        #takes a word and returns a list of words with Damerau-Levenshtein distance of 1
        lst_insertion = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for pos in range(len(word) +1):
            for letter in alphabet:
                a = list(word)
                a.insert(pos, letter)
                res = "".join(a)
                lst_insertion.append(res)
        return lst_insertion


    def deletion(self, word):
        lst_deletion = []
        for pos in range(len(word)):
            res = word[:pos] + word[pos+1:]
            lst_deletion.append(res)
        return lst_deletion


    def substitution(self, word):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        lst_substitution = []
        for pos in range(len(word)):
            for letter in alphabet:
                if letter != word[pos]:
                    res = word[:pos] + letter + word[pos+1:]
                    lst_substitution.append(res)
        return lst_substitution



    def swapping(self, word):
        lst_swapping = []
        for i in range(len(word)-1):
            a = list(word)
            a[i], a[i+1] = a[i+1], a[i]
            res = "".join(a)
            lst_swapping.append(res)
        return lst_swapping


    def combine(self, word):
        #combines the suggestions from the 4 edit methods into a set, returns the set
        lst_insertion = self.insertion(word)
        lst_deletion = self.deletion(word)
        lst_substitution = self.substitution(word)
        lst_swapping = self.swapping(word)
        set_combine = set()
        for i in lst_insertion:
            set_combine.add(i)
        for i in lst_deletion:
            set_combine.add(i)
        for i in lst_substitution:
            set_combine.add(i)
        for i in lst_swapping:
            set_combine.add(i)
        return set_combine


def get_lines(path):
    with open(path, "r") as f:
        lines = f.read()
        return lines


def get_bigram(lines):
    bigram_dict = defaultdict(int)
    for i in range(len(lines) -1):
        pair = lines[i], lines[i+1]
        bigram_dict[pair] += 1
    sorted_list = sorted(bigram_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_list
    #populates a dict:
    #keys = bigrams
    #values = their frequency from a corpus
    #transforms dict into list of tuples (containing bigrams and their associated frequencies), sorts this list by frequency in descending order



def main():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lexicon = read_lexicon(sys.argv[1])
    auto = AutoCorrect(lexicon, alphabet)
    #build the bigram frequency model from a corpus:
    corpus = get_lines(sys.argv[2])
    tokenized_corpus = word_tokenize(corpus)
    bigram = get_bigram(tokenized_corpus)

    message_so_far = ""

    while True:
        #ask the user to type in a word
        print("Type in a word: ")
        word = input()
        l = []
        if word in lexicon:
            #check if word is spelled correctly (using the lexicon)
            for i in bigram:
                #suggesting next word (based on bigram frequencies)
                if i[0][0] == word:
                    l.append(i)
            sorted_counts = sorted(l, key=lambda x:x[1], reverse=True)
            top_counts = sorted_counts[:3]
            counter = 0
            print("Either select a word")
            for t in top_counts:
                print(f"{counter}: {t[0][1]}")
                counter += 1
            print("or type something else: ")
            input_user = input()
            if input_user.isdigit():
                #if the user choose one of the 3 suggested words
                input_user = int(input_user)
                chosen_word = top_counts[input_user][0][1]
                message_so_far = message_so_far + " " + chosen_word
                print(f"Your message so far is: {message_so_far}")
            else:
                #if user choose another word
                message_so_far = message_so_far + " " + input_user
                print(f"Your message so far is: {message_so_far}")
        else:
            #if the word is spelled incorrectly
            suggestions = []
            suggested_words = []
            random_words = []
            suggested_words_2 = []
            suggest = auto.combine(word)
            for w in suggest:
                if w in lexicon:
                    #gather the possible suggestions for a word at distance 1 from the words in the lexicon
                    suggestions.append(w)
            if not suggestions:
                #if word is not in lexicon (even when trying to correct it) suggest 3 random words
                counter = 0
                print("That word is not in the lexicon. Here are random suggestions for the next word: ")
                random_words = random.sample(list(lexicon), 3)
                for r in random_words:
                    print(f"{counter}: {r}")
                    counter += 1
                print("or type something else: ")
                input_user = input()
                if input_user.isdigit():
                    #if the user choose one of the 3 suggested words
                    input_user = int(input_user)
                    chosen_word = random_words[input_user]
                    message_so_far = message_so_far + " " + chosen_word
                    print(f"Your message so far is: {message_so_far}")
                else:
                    #if the user chooses another word
                    message_so_far = message_so_far + " " + input_user
                    print(f"Your message so far is: {message_so_far}")
            else:
                #if there is correct word at distance 1 from the input word, suggest that word
                suggested_word = suggestions[0]
                print(f"Did you mean {suggested_word} ? y/n")
                user_input = input()
                while user_input == "n":
                    suggested_words_2 = random.sample(suggestions, min(3, len(suggestions)))
                    print(f"Did you mean {suggested_words_2} ? y/n")
                    user_input = input()
                if user_input == "y":
                    message_so_far = message_so_far + " " + suggested_word
                    print(f"Your message so far is: {message_so_far}")


main()



