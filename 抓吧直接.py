import urllib.request
import urllib.error

# for x in range(1, 82, 2):
#     for y in range(1, 82, 1):
#         try:
#             urllib.request.urlretrieve(f'https://t1.hddhhn.com/uploads/tu/202002/{x}/{y}.jpg',\
#                 f'c:/Users/ASUS/Pictures/联想爬虫/{x}--{y}.jpg')
#         except urllib.error.HTTPError:
#             break


# https://t1.hddhhn.com/uploads/tu/201904/403/11.jpg

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

for x in range(1, 100, 1):
    try:
        urllib.request.urlretrieve(f'https://t1.hddhhn.com/uploads/tu/202002/79/{x}.jpg',\
            f'c:/Users/ASUS/Pictures/联想爬虫/二/二{x}.jpg')
    except urllib.error.HTTPError:
        break