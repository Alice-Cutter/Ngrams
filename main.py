from ngrams import getOneGrams, getTwoGrams, printTopN

def main():
    filename = "Hamlet.txt"
    #oneGramDict = getOneGrams(filename, True)
    twoGramDict = getTwoGrams(filename)
    printTopN(twoGramDict, 10)

if __name__ == '__main__':
    main()
