while 1 :
    from calendar import *
    year = int(input('输入年：'))
    month = int(input('输入月：'))
    day = int(input('输入日：'))
    aweek = {0:'周一',1:'周二',2:'周三',3:'周四',4:'周五',5:'周六',6:'周日'}
    if str(year).isdigit() and str(month).isdigit() and str(day).isdigit() and 1<=month<=12 and 1<=day<=31 :
        p = weekday(year,month,day)
        print('{0}年{1}月{2}日是{3}'.format(year,month,day,aweek.get(p)))
    else:
        ('输入日期错误，滚。')