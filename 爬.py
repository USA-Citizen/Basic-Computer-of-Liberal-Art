import urllib.request
import re

def getHttp(url):
    h = urllib.request.urlopen(url)
    html = h.read()
    return html

# url[5:-1]部分必须是一个可以打开的图片网址！
def downloadImg(html):
    reg = r'src="https.*?\.jpg"'
    imgre = re.compile(reg)
    urls = imgre.findall(html)
    x = 0
    for url in urls:
        urllib.request.urlretrieve(url[5:-1], 'c:/Users/ASUS/Pictures/联想爬虫/%s.png'%x)
        x += 1

def main():
    html = getHttp('https://www.2717.com/ent/meinvtupian/').decode('GBK')
    downloadImg(html)

if __name__ == '__main__':
    main()