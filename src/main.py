from nltk.corpus import wordnet
import urllib2, json, time, re, itertools
from bs4 import BeautifulSoup
from StopWords import *

def fetchPage(url):
    u = urllib2.urlopen(url)
    htmlPage = u.read()
    htmlPage = BeautifulSoup(htmlPage)

    div_content = htmlPage.find("div", { "id" : "content" })
    spans = div_content.findAll("span")

    sheldon_words = []
    for span in spans:
        speech = str(span.text.encode('utf8'))
        match = re.match(r'^Sheldon', speech, re.I)
        if match:
            terms = list(set(re.findall('[a-z]+', speech.lower())))
            sheldon_words.extend(terms)
    sheldon_words = sorted(list(set(sheldon_words)))
    return sheldon_words

def getWords():
    urls = open('../data/config/trans_urls.txt', 'r').read().split('\n')
    outfile = open('../data/config/sheldon_words.txt', 'w')
    urls = urls[:len(urls)-1]
    for url in urls:
        print url
        words = fetchPage(url)
        for word in words:
            outfile.write(word + '\n')
    outfile.close()

def sortWords():
    stopwords = StopWords('../data/config/stopwords.txt').getStopWords()
    names_males = StopWords('../data/config/names_males.txt').getStopWords()
    names_females = StopWords('../data/config/names_females.txt').getStopWords()

    wordsFile = open('../data/output/sheldon_words.txt', "r")
    text = wordsFile.read()
    wordsFile.close()
    words = list(set(re.findall('[a-z]+', text.lower())))
    words = sorted(list(set(words) - set(stopwords)))
    words = sorted(list(set(words) - set(names_males)))
    words = sorted(list(set(words) - set(names_females)))
    outfile = open('../data/output/sorted_sheldon_words.txt', 'w')
    for word in words:
        if len(word) > 2:
            #synsets = wordnet.synsets(word)
            #for synset in synsets:
                #if synset.lemmas[0].name == word:
                    #outfile.write(word + ':' + synset.definition + '\n')
            outfile.write(word+'\n')
    outfile.close()

if __name__ == "__main__":
    #getWords()
    sortWords()
