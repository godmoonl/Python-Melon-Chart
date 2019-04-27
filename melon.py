class Melon:
    def __init__(self):
        url = 'http://www.melon.com/chart/index.htm'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url,headers=hdr)
        response = urlopen(req)
        soup = BeautifulSoup(response,'html.parser')
        tag = []
        a = []
        for t in soup.find_all('tr',class_='lst50'):
            tag.extend(t.find('div',class_='wrap_song_info').find_all('a')[:1])
            a.extend(t.find('div',class_='wrap_song_info').find_all('a')[2:])
        if __name__ == "__main__":
            for i in range(50):
                print(i+1,tag[i].text,a[i].text)
        self.tag=tag
        self.a=a
if __name__ == "__main__":
    Melon()
