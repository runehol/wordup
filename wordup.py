#!/usr/bin/env python3
import sys
import filereader
import tokenizer
import french
import uniquify
import read_known_file



def main(argv = sys.argv):
    lang = french.FrenchModule()


    known_words = read_known_file.read_known_file("french_known_words.txt", lang) | read_known_file.read_known_file("french_ignore_list.txt", lang)

    uw = uniquify.UniqueWords()
    for fname in argv[1:]:
    
        data = filereader.read_file(fname)
        tokens = tokenizer.tokenize(data)
    
        uw.uniquify(tokens, lang)

    uniquify.rank(uw, lang, known_words)



if __name__ == "__main__":
    main()
    
