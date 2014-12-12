#!/usr/bin/env python3
import sys
import srtreader
import tokenizer
import french
import uniquify
import read_known_file



def main(argv = sys.argv):
    lang = french.FrenchModule()


    known_words = read_known_file.read_known_file("french_known_words.txt", lang) | read_known_file.read_known_file("french_ignore_list.txt", lang)
    
    data = srtreader.read_srt(argv[1])
    tokens = tokenizer.tokenize(data)
    ut = uniquify.uniquify(tokens, lang)
    uniquify.rank(ut, lang, known_words)



if __name__ == "__main__":
    main()
    
