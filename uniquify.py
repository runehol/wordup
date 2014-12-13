
import collections


class UniqueWords:
    def __init__(self):
        self.word_count = 0
        self.stems = dict()


    def reg_word(self, stem, word, sentence, blockname, textname):
        self.word_count += 1

        uw = self.stems.get(stem)
        if uw is None:
            uw = UniqueWord(stem)
            self.stems[stem] = uw

        uw.reg_word(word, sentence, blockname, textname)


    def uniquify(self, tokens, lang):
        for (word, sentence, blockname, textname) in tokens:
            stem = lang.stem(word)
            self.reg_word(stem, word, sentence, blockname, textname)


        
class UniqueWord:

    def __init__(self, stem):
        self.stem = stem
        self.word_freqs = collections.defaultdict(int)
        self.word_examples = dict()
        self.count = 0

    def reg_word(self, word, sentence, blockname, textname):
        if not word in self.word_examples:
            self.word_examples[word] = (sentence, blockname, textname)

        self.word_freqs[word] += 1
        self.count += 1

    def get_variants(self):
        t = [(v, k) for k, v in self.word_freqs.items()]
        t.sort(reverse=True)
        return t

    def repr_word(self):
        t = self.get_variants()
        if len(t):
            # try to get a lower-case word if possible
            idx = 0
            while idx < len(t) - 1 and t[idx][1].istitle():
                idx += 1
                
            
            return t[idx][1]


    def get_example(self):
        word = self.repr_word()
        sentence, blockname, textname = self.word_examples[word]
        return (word, sentence, blockname, textname)




def rank(unique_words, lang, known_words):
    t = [(uw.count, uw.stem, uw) for uw in unique_words.stems.values()]
    t.sort(reverse=True)
    accum_count = 0
    word_count = unique_words.word_count
    scalefac = 100.0/word_count
    for entry in t:
        uw = entry[2]
        count = uw.count

        if uw.stem not in known_words:
            variants = uw.get_variants()
            if lang.is_interesting(variants):
                word, sentence, blockname, textname = uw.get_example()
                accum_percent = scalefac*accum_count
            
                print("%.2f\t%.2f\t%s\t%s\t%s %s" % (accum_percent, count*scalefac, word, sentence, textname, blockname))

        accum_count += count
