#!/usr/bin/env python3


from bs4 import BeautifulSoup
import sys
import urllib.request
import http.cookiejar
import re



def fetch_alarabiya_cookie(url):
    webpage = urllib.request.urlopen(url).read()
    m = re.search(b"setCookie\('([^']*)', '([^']*)'", webpage)
    if m:
        return m.group(1).decode("utf-8"), m.group(2).decode("utf-8")



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

    res = fetch_alarabiya_cookie(url)
    if not res: raise IOError()



    cj = http.cookiejar.CookieJar()
    ck = http.cookiejar.Cookie(version=0, name=res[0], value=res[1], port=None, port_specified=False, domain='english.alarabiya.net', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
    cj.set_cookie(ck)

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(url)
    webpage = r.read()

    soup = BeautifulSoup(webpage)

    video_url = None
    

    t = soup.find('div', {"class" : "jwEn"})
    if t:
        extract_and_write_subtitle(t, out_stub_name + "_en.srt")

    t = soup.find('div', {"class" : "jwAr"})
    if t:
        extract_and_write_subtitle(t, out_stub_name + "_ar.srt")

    t = soup.find('meta', {'property' : 'videoURL'})
    if t:
        video_url = t.get('content')
        print(video_url)
        download(video_url, out_stub_name + ".mp4")



if __name__ == "__main__":
    scrape_alarabiya(sys.argv[1], sys.argv[2])
