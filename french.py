
import nltk.stem
import nltk.stem.snowball

class FrenchModule:
    def __init__(self):
        self.stemmer = nltk.stem.snowball.SnowballStemmer("french", ignore_stopwords=True)

    def stem(self, word):
        return self.stemmer.stem(word)


    def is_interesting(self, variants):
        #frequency, word
        if len(variants) > 1: return True
        count, word = variants[0]
        if not word.istitle(): return True
        if count <= 2: return True
        return False
