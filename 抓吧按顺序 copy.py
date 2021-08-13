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
    for url in urls:
        urllib.request.urlretrieve(url[5:-1], f'c:/Users/ASUS/Pictures/联想爬虫/{x}.jpg')
        break

def main():
    for x in range(2,50):
        html = getHttp(f'https://www.2717.com/ent/meinvtupian/2020/316485_{x}.html').decode('GBK')
        reg = r'src="https.*?\.jpg"'
        imgre = re.compile(reg)
        urls = imgre.findall(html)
        for url in urls:
            urllib.request.urlretrieve(url[5:-1], f'c:/Users/ASUS/Pictures/联想爬虫/{x}.jpg')
            break
        

if __name__ == '__main__':
    main()

# https://t1.hddhhn.com/uploads/tu/202002/9/1.jpg