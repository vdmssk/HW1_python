tr = int(input()); #кол-во поездок
p = tr // 60 #60 поездок
d = tr % 60 // 10 #10 поездок
n = tr % 10 #1 поездка 


#проверка; если больше 1, берем 10
if n * 15 > 125:
    n = 0
    d += 1
#если больше 10,берем 60

if n * 15 + d * 125 > 440:
    n = 0
    d = 0
    p += 1
print(n, d, p);