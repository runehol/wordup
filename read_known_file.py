import csv
import nltk.tokenize



def read_known_file(filename, lang):
    res = set()
    f = open(filename, encoding="utf-8")
    reader = csv.reader(f, delimiter="\t")

    tokenizer = nltk.tokenize.RegexpTokenizer(u"[\s\.:{},?!\"،؟\d]+", gaps=True)
    word_tokenize = tokenizer.tokenize
    for row in reader:
        if len(row):
            words = word_tokenize(row[0])
            for w in words:
                s = lang.stem(w)
                
                res.add(s)
    return res
