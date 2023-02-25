a = int(input()) # / число на единицы c & десятки b
b = a // 10
c = a % 10


#десятки
if b == 10:
    result = "C"
elif b == 9:
    result = "XC"
elif b == 4:
    result = "XL"
elif b >= 5:
    result = "L" + (b - 5)*"X"
else:
    result = b*"X"


#единицы
if c == 9:
    result += "IX"
elif c == 4:
    result += "IV"
elif c >= 5:
    result += "V" + (c - 5)*"I"
else:
    result += c*"I"
print(result)