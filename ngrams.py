# ngrams.py
# A program that tallies n-gram counts in given text files
# CS 111 - Eric Alexander
# <YOUR NAME(S) HERE>

def getOneGrams(filename, stopWords):
    ''' Function takes in a given text filename and counts one-grams in the file '''
    
    oneGramCounts = {}
    with open("stopwords.txt", 'r') as f:
      for line in f:
              # Clean out punctuation
              for ch in '!@#$%^&*()_+-=;:",./<>?\\':
                  line = line.replace(ch, ' ')

              # Reduce to all lowercase
              line = line.lower()

              # Split into words
              stopWordsList = line.split()

    with open(filename, 'r') as f:
        for line in f:
            # Clean out punctuation
            for ch in '!@#$%^&*()_+-=;:",./<>?\\':
                line = line.replace(ch, ' ')

            # Reduce to all lowercase
            line = line.lower()

            # Split into words
            words = line.split()
            
            # Add to oneGramCounts for each word (checking to see if it is already present)
            for word in words:
              if stopWords == True:
                if not word in stopWordsList:
                  if word in oneGramCounts:
                      oneGramCounts[word] += 1
                  else:
                      oneGramCounts[word] = 1
              else:
                if word in oneGramCounts:
                  oneGramCounts[word] += 1
                else:
                  oneGramCounts[word] = 1
    return oneGramCounts

def getTwoGrams(filename):
    twoGramCounts = {}
    with open(filename, 'r') as f:
        for line in f:
            # Clean out punctuation
            for ch in '@#$%^&*()_+-=;:",/<>\\':
                 line = line.replace(ch, ' ')
            for ch in '.!?':
                 line = line.replace(ch, ' {} '.format(ch))
            # Reduce to all lowercase
            line = line.lower()
                    
            # Split into words
            words = line.split()
            
            # Add to oneGramCounts for each word (checking to see if it is already present)
            # while iterating through the list of words 
              # check to see if words[i]
            for i in range(len(words) - 1): 
              foo = (words[i], words[i + 1])
              if foo in twoGramCounts:
                if foo[word[[i + 2]] in ngramsToNext:
                  ngramsToNext[foo][word[i + 1]] += 1
                twoGramCounts[foo] += 1
              else:
                twoGramCounts[foo] = 1

    return twoGramCounts

def printTopN(countDict, n):
    ''' Function takes a dictionary mapping n-grams to counts and prints top n n-grams by count. '''

    dictItems = list(countDict.items())
    dictItems.sort(key=lambda pair: pair[1], reverse=True)

    for i in range(n):
        word, count = dictItems[i]
        print('{} {}'.format(word, count))
