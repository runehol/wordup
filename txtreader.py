import os.path


def read_file(filename):
    f = open(filename, encoding="utf-8")
    blocks = []



    txt = f.read()
    txt = txt.replace("\n", " ")
    txt = txt.replace("\r", " ")
    
    blocks.append(("", txt))

    pname = os.path.splitext(os.path.basename(filename))[0]

    return (pname, blocks)
