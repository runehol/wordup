import os.path


def read_file(filename):
    f = open(filename, encoding="utf-8")
    blocks = []

    NR, TIMESTAMP, TEXT = range(3)
    state = NR
    timestamp = ""
    txt = ""
    for line in f:

        while len(line) and (line[-1] == "\n" or line[-1] == "\r"):
            line = line[:-1]
        if state == NR:
            state = TIMESTAMP
        elif state == TIMESTAMP:
            timestamp = line
            state = TEXT
        elif state == TEXT:
            if line == "":
                blocks.append((timestamp, txt))
                txt = ""
                state = NR
            else:
                if txt != "": txt += " "
                txt += line

    pname = os.path.splitext(os.path.basename(filename))[0]

    return (pname, blocks)
