import re

class TokenHandler:
	
	def __init__(self, text):
		self.text = text
		self.wordFreq = {}
	
	def getWords(self):
		words = re.findall(r'[a-z0-9@#$%*&!]+', self.text)
		return words
	
	def getUniqueWords(self):
		words = list(set(self.getWords(self.text)))
		return words
	
	def getWordsFreq(self):
		self.wordList = self.getWords()
		for word in self.wordList:
			self.wordFreq[word] = 1 + self.wordFreq.get(word, 0)
		return self.wordFreq

	def getNGramWordsList(self, n=2):
		nGramList = []
		lines = self.text.split("\n")
		for line in lines:
			words = self.getWords(line)
			for i in range(0, len(words)-1):	
				tempString = ""
				tempString += words[i:i+n] + " "
				nGramList.append(tempString.strip())
		return nGramList
