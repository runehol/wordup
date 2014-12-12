#!/usr/bin/env python3
import sys
import srtreader
import tokenizer


def main(argv = sys.argv):
    
    data = srtreader.read_srt(argv[1])
    tokens = tokenizer.tokenize(data)



if __name__ == "__main__":
    main()
    
