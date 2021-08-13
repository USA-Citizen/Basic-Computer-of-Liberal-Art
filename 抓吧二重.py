import urllib.request
import urllib.error

for x in range(1, 82, 2):
    for y in range(1, 82, 1):
        try:
            urllib.request.urlretrieve(f'https://t1.hddhhn.com/uploads/tu/202002/{x}/{y}.jpg',\
                f'c:/Users/ASUS/Pictures/联想爬虫/{x}--{y}.jpg')
        except urllib.error.HTTPError:
            break
