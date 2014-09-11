import re

class StopWords:

    def __init__(self, fileName='../data/config/stopwords.txt'):
        self.fileName = fileName

    def getStopWords(self):
        stopWordsFile = open(self.fileName, "r")
        text = stopWordsFile.read()
        stopWordsFile.close()
        self.stopWordList = list(set(re.findall('[a-z]+', text.lower())))
        return self.stopWordList

