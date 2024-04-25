# импортируем модули f_a и f_x из пакета paket
from paket import f_a, f_x


n = 10
x = 5
b = f_a.mysp(x,n) # функция из модуля f_a
print(b)

c = f_a.initsp(5, 10, 21) # функция из модуля f_a
print(c)

xx = 0.5
s = f_x.func(x)  # функция из модуля f_x
print(s)

a, b, c = 3, 4, 5 # стороны треугольника
s_tr = f_x.tr(a, b, c) # функция из модуля f_x
print(s_tr)

a, b = 3, 5 # стороны прямоугольника
p, s = f_x.pram(a, b) # функция из модуля f_x
print(p, s)


