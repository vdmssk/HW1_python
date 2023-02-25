a = float(input());
b = float(input());
x = float(input());
y = (b ** 2) - (4 * a * x);


if y > 0:
#0.5 ибо ищем корень
    x1 = (-b + (y ** 0.5)) / (2 * a);
    x2 = (-b - (y ** 0.5)) / (2 * a);
    print(x1, x2);

if y < 0:
    print('');
elif y == 0:
    print((-b) / (2 * a));