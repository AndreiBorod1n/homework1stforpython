print("Введите трехзначное число:")
a = input()
a = int(a)
frstnum = a/100
frstnum = int(frstnum)
b = (a - (frstnum*100))
b = int(b)
sndnum = b/10
sndnum = int(sndnum)
trstnum = b - (sndnum*10)
print(frstnum,sndnum,trstnum)
finishnum = frstnum+sndnum+trstnum
print("Сумма цифр в трехзначном числе:")
print(finishnum)
