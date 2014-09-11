import re
import urllib2
import sys
import sdictviewer.formats.dct.sdict as sdict
import sdictviewer.dictutil

def get_google_url(search, siteurl=False):
    if siteurl == False:
        return 'http://www.google.com/search?q=' + urllib2.quote(search)
    else:
        return 'http://www.google.com/search?q=site:' + urllib2.quote(siteurl) + '%20' + urllib2.quote(search)

def get_google_data(search, siteurl = False):
    #google returns 403 without user agent
    headers = {'User-agent':'Mozilla/11.0'}
    req = urllib2.Request(get_google_url(search, siteurl), None, headers)
    site = urllib2.urlopen(req)
    data = site.read()
    html = data.decode('ascii', 'ignore')
    site.close()

    #no_of_res = re.findall(r'About (.*?)? results', html)
    no_of_res = re.findall(r'About (.*?) results', html)
    no_of_res = str(no_of_res[0]).replace(',', '')
    print no_of_res
    #print get_def(search)

def get_def(start_word):
    dictionary = sdict.SDictionary('../data/config/oxford.dct')
    #dictionary = sdict.SDictionary('../data/config/MWCollegiate.dct')
    #dictionary = sdict.SDictionary('../data/config/webster_1913.dct')
    dictionary.load()

    found = False
    for word in dictionary.get_word_list_iter(start_word):
        try:
            if start_word == str(word):
                instance, definition = word.read_articles()[0]
                return [start_word, definition]
        except:
            continue

    dictionary.close()
    return found

get_google_data('canny')
