import urllib.request
import urllib.error
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
    lxxlist = ['20200225_18582_',
'20200220_18553_',
'20200216_18522_',
'20200215_18509_',
'20200125_18370_',
'20200119_18327_',
'20200116_18312_',
'20200115_18305_',
'20200111_18281_',
'20200108_18255_',
'20200107_18248_',
'20200102_18219_']
    for y in lxxlist:
        for x in range(2, 100, 1):
            try:
                html = getHttp(f'https://m.yeitu.com/meinv/xinggan/{y}{x}.html').decode('utf-8', 'ignore')
                reg = r'src="https.*?\.jpg"'
                imgre = re.compile(reg)
                urls = imgre.findall(html)
                for url in urls:
                    urllib.request.urlretrieve(url[5:-1], f'c:/Users/ASUS/Pictures/联想爬虫/{y}{x}.jpg')
                    break
            except urllib.error.HTTPError:
                break
        

if __name__ == '__main__':
    main()

    # https://www.yeitu.com/meinv/xinggan/20191231_18205_93.html

# lxx
# https://m.yeitu.com/meinv/xinggan/20200225_18582_2.html
# https://m.yeitu.com/meinv/xinggan/20200220_18553_2.html
# https://m.yeitu.com/meinv/xinggan/20200216_18522_2.html
# https://m.yeitu.com/meinv/xinggan/20200215_18509_32.html
# https://m.yeitu.com/meinv/xinggan/20200125_18370_2.html
# https://m.yeitu.com/meinv/xinggan/20200119_18327_2.html
# https://m.yeitu.com/meinv/xinggan/20200116_18312_2.html
# https://m.yeitu.com/meinv/xinggan/20200115_18305_2.html
# https://m.yeitu.com/meinv/tiyumeinv/20200111_18281_2.html
# https://m.yeitu.com/meinv/xinggan/20200108_18255_2.html
# https://m.yeitu.com/meinv/xinggan/20200107_18248_2.html
# https://m.yeitu.com/meinv/xinggan/20200102_18219_2.html


