#!/usr/bin/env python3
import sys
import srtreader
import tokenizer
import french
import uniquify



def main(argv = sys.argv):

    lang = french.FrenchModule()
    data = srtreader.read_srt(argv[1])
    tokens = tokenizer.tokenize(data)
    ut = uniquify.uniquify(tokens, lang)
    uniquify.rank(ut)


if __name__ == "__main__":
    main()
    
