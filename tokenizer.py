
import nltk.tokenize


def tokenize(data):
    textname = data[0]
    blocks = data[1]

    sent_tokenize = nltk.tokenize.sent_tokenize

    tokenizer = nltk.tokenize.RegexpTokenizer(u"[\s\.,-?!'\"،؟\d·•—()×«]+", gaps=True)
    word_tokenize = tokenizer.tokenize

    
    for block in blocks:
        blockname = block[0]
        text = block[1]
        sentences = sent_tokenize(text.strip())
#        print(sentences)
        for sentence in sentences:
            words = word_tokenize(sentence)
#            print(words)
            for word in words:
                yield (word, sentence, blockname, textname)
