#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# FileName : crawlData.py
# Date : Thu Sep 11 22:58:19 2014
# Author : prempraveen
# Last Modified:
#
# Copyright © 2014 prempraveen <prempraveen@PremPraveens-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""

import urllib2

def crawlData():
    urls = open('../data/config/trans_urls.txt', 'r').read().split('\n')
    urls = urls[:len(urls)-1]
    for url in urls:
        print url
        u = urllib2.urlopen(url)
        htmlPage = u.read()
        outfile = open('../data/input/' + url[:-1].split('/')[-1] + '.txt', 'w')
        outfile.write(htmlPage)
        outfile.close()


'''
def extractCharacters():
    #Extract characters from each episode
def extractCharacterSpeeches(character):
    #Extract character's speeches from each episode
def extractCharacterWords(character):
    #From character's speeches extract characters's words, word count, unique words,
    #unique words freq, common words[with and without stop words]
def extractCharacterUniqueWordForms(character):
    #From character's speeches extract character's unique stemmed words
def extractPositiveWords(character):
    #From character's speeches extract character's positive words
def extractNegativeWords(character):
    #From character's speeches extract character's negative words
def extractOtherCharacterMentions(character):
    #From character's speeches extract character's other characters in the sitcom mentions,
    #famous personalities in general.
'''

'''
def generateEpisodeData():

def generateSeasonData():

def generateCompleteData():

'''

'''
def extractCompleteDataWords():
    #Extract words, word count, unique words,
    #unique words freq, common words[with and without stop words]
def extractCompleteDataSpeeches():
    #Extract speeches from each complete Data, speech length, speech by
def extractCharacterReferences():
    #Extract famous personalities mentions
def extractCharacterRelationships():
    #Extract characters mentions by all the characters
def extractWordTypes():
    #Extract technical, slang
'''
crawlData()

