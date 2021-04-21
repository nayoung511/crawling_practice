"""
Python-2
Create a program to read a text file with various tweets. 
The output should be 2 text files: 

- the first should contain the list of all unique words 
   among all tweets along with the count for repeated words;

- the second should contain the median amount of unique words 
   across all the tweets.
"""

import itertools
from collections import Counter
import re

"""
input: tuple
output: String
"""
def makeStr(tup):
    value = "".join(map(str, tup))
    return value


#read a text file
f = open("input.txt", "r")
content = f.read()
f.close()

#split lines
lines = content.split("\n")

#extract each word
words = []
for i in range (len(lines)):
    words.append(lines[i].split())
words = list(itertools.chain(*words))   #flatten the lists

count_words =[]
for i in range (len(words)):
    regex = re.compile('[^0-9a-zA-Z_-]')
    cleansed_word = regex.sub('',words[i].lower())

    #Accept only string that is not symbol e.g) -, _
    if cleansed_word != "-" or cleansed_word != "_":
        count_words.append(cleansed_word)

#Extract frequency of each word (Descending Order)
#format: (word, frequency)
#type: Tuple
count_words = Counter(count_words).most_common()



# output 1 - contain the list of all unique words 
#            among all tweets along with the count for repeated words

f = open("output1.txt", "w+")
header = 'No.\t|\tUnique Words\t|\tFrequency\n'
f.write(header)
f.write("-----------------------------------------\n")

for i in range (len(count_words)):
    f.write("{:<10}{:<20}{:<15}\n".format(i+1, makeStr(count_words[i][0]), str(count_words[i][1])))
f.close()


# output 2 - the second should contain the median amount of unique words 
#            across all the tweets.

f = open("output2.txt", "w+")
header = 'Uniquie Words\t|\tFreqency\n'
f.write(header)
f.write("---------------------------------\n")
f.write("{:<25}{:<15}\n".format(makeStr(count_words[len(count_words)//2][0]), str(count_words[len(count_words)//2][1])))
f.close()
