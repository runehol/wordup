#!/usr/bin/env python3
import sys
import filereader
import tokenizer
import arabic
import french
import uniquify
import read_known_file
import errno



def main(argv = sys.argv):

    argv = argv[1:]
    
    if len(argv) and argv[0] == "--arabic":
        argv = argv[1:]
        lang = arabic.ArabicModule()
        known_words = read_known_file.read_known_file("arabic_known_words.txt", lang) | read_known_file.read_known_file("arabic_ignore_list.txt", lang)
    else:
        lang = french.FrenchModule()
        known_words = read_known_file.read_known_file("french_known_words.txt", lang) | read_known_file.read_known_file("french_ignore_list.txt", lang)
        

    uw = uniquify.UniqueWords()
    for fname in argv:
    
        data = filereader.read_file(fname)
        tokens = tokenizer.tokenize(data)
    
        uw.uniquify(tokens, lang)

    uw.weed_out_uninteresting_words(lang)

    uniquify.rank(uw, lang, known_words)



if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except BrokenPipeError:
            pass

        

    
