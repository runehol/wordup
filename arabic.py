
import nltk.stem
import nltk.stem.snowball
import re


class ArabicModule:
    def __init__(self):
        self.stemmer = nltk.stem.ISRIStemmer()
        self.ar_regexp = re.compile(u"[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufc3f]|[\ufe70-\ufefc]")

    def stem(self, word):

        # a bit of pre-handling to fix the Levantine dialect convention of writing hal first
        if len(word) >= 5 and word.startswith("هال"): word = word[1:]
        
        return self.stemmer.stem(word)


    def is_interesting(self, variants):

        #frequency, word


        #this filter looks for at least one arabic character

        for count, word in variants:
            if self.ar_regexp.search(word): return True

        
        return False
