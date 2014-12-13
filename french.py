
import nltk.stem
import nltk.stem.snowball

class FrenchModule:
    def __init__(self):
        self.stemmer = nltk.stem.snowball.SnowballStemmer("french", ignore_stopwords=True)

    def stem(self, word):
        return self.stemmer.stem(word)


    def is_interesting(self, variants):


        #frequency, word


        #this filter is aimed at filtering out proper names, because they shouldn't go into vocab lists

        totalcount = 0
        for count, word in variants:
            if not word.istitle() and not word.isupper(): return True
            totalcount += count


        if totalcount <= 2: return True

        
        return False
