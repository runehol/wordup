
import nltk.stem
import nltk.stem.snowball

class FrenchModule:
    def __init__(self):
        self.stemmer = nltk.stem.snowball.SnowballStemmer("french", ignore_stopwords=True)

    def stem(self, word):
        return self.stemmer.stem(word)
