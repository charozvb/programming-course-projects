#Project Title:
The relation between phonetic clarity and information density

##Project description
The projects starts off the observation that when people produce speech that carries less information (lower surprisal), they tend to speak less clearly (so with shorter duration). On the contrary, when people produce more information (higher surprisal), they tend to articulate more clearly (meaning they take longer to speak, so longer duration). This project tries to replicate this observation by creating speech data and show if there is a relation between word duration and surprisal.


The following files and their respective functions where implemented:
get durations.py: calculates the duration in ms for each orthographic word
get surprisals.py: calculates the average surprisal over a sentence, also creates unigrams and bigrams
get linear model.py: creates a linear regression model to explain the variability of duration as a function of surprisal, using a file that contains the duration and the surprisal for each sentence
get histogram.py: creates a histogram of the duration on the x axis and their frequencies on the y axis

##Data
The data was collected by creating 10 sentences that only contained bigrams already present in our bigram dictionary. These sentences were recorded and their durations were collected using MAUS. Thus each sentence had a csv files containing the durations of each word. 

##How to run+use the project
For the project, you can use new sentences again and record them or use the ones already present. Then you need to calculate their durations using the get durations.py file. After that, with the get surprisals.py file you can calculate the surprisal for each sentence. With the linear model you can create a plot to visually show if there is any relation between the duration and the surprisal. Additionally,you can visualize the findings from the linear regression model using the get histogram.py file.


