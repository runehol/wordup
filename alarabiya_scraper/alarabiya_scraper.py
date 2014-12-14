#!/usr/bin/env python3


from bs4 import BeautifulSoup
import sys
import urllib.request
# http://english.alarabiya.net/en/webtv/news-bulletin/2014/12/11/1300GMT.html




def download(url, file_name):
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    file_size = int(u.getheader("Content-Length"))
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        sys.stdout.write(status,)
        sys.stdout.flush()

    f.close()


def extract_and_write_subtitle(elem, fname):
    print(fname)

    contents = []
    starttimes = []
    stoptimes = []
    
    for line in elem.findAll("div", {"class":"line"}):
        starttime = line["data-start"]
        content = line.a.contents[0]
        contents.append(content)
        starttimes.append(starttime)

    if len(starttimes):
        stoptimes = starttimes[1:]
        lastbeginning = starttimes[-1]
        #let's arbitrarily add a minute to this one
        exploded = list(lastbeginning.split(":"))
        exploded[1] = str(int(exploded[1]) + 1)
        lastend = ":".join(exploded) #yeah, that'll do
        stoptimes.append(lastend)

    #now write this thing out

    f = open(fname, "w", encoding="utf-8")

    for i in range(len(starttimes)):
        f.write("%d\n" % (i+1,))
        f.write("%s --> %s\n" % (starttimes[i], stoptimes[i]))
        f.write(contents[i])
        f.write("\n\n")

    f.close()

        


def scrape_alarabiya(url, out_stub_name):
    #webpage = urllib.request.urlopen(url).read()
    webpage = open("alarabiya_scraper/test.html", "rb").read()

    soup = BeautifulSoup(webpage)

    video_url = None
    
    t = soup.find('meta', {'property' : 'videoURL'})
    if t:
        video_url = t.get('content')
        print(video_url)
        #download(video_url, out_stub_name + ".mp4")

    t = soup.find('div', {"class" : "jwEn"})
    if t:
        extract_and_write_subtitle(t, out_stub_name + "_en.srt")

    t = soup.find('div', {"class" : "jwAr"})
    if t:
        extract_and_write_subtitle(t, out_stub_name + "_ar.srt")




if __name__ == "__main__":
    scrape_alarabiya(sys.argv[1], "alarabiya20141211_1300")
