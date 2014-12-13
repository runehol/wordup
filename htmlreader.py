import os.path
from html.parser import HTMLParser

class TextExtractParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
    def handle_data(self, data):
        self.items.append(data)

def parse_html(pname, content):

    parser = TextExtractParser()
    parser.feed(content)
    for item in parser.items:
        yield item, "", pname
        

def read_file(filename):
    pname = os.path.splitext(os.path.basename(filename))[0]

    f = open(filename, encoding="utf-8")
    data = f.read()
    yield from parse_html(pname, data)


