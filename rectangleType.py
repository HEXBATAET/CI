inpText = input('Введите длины сторон треугольника через пробел')

try:
    temp = inpText.split(' ')
    if len(temp) != 3:   
        raise Exception("кол-во аргументов не равно трём")
    temp = sorted([float(i) for i in temp])  
    if any(i<=0 for i in temp):  
        raise Exception('длина <= 0')   
    a,b,c = temp

except BaseException as err:
    print('Неверные входные данные ' + err.args[0])
    exit()

if c > a + b:
    print('impossible')
    exit() 

if c*c == a*a+b*b:
    print('rectangular')
    exit()
if c*c < a*a+b*b:
    print('acute')
    exit()
if c*c > a*a+b*b:
    print('obtuse')
    exit()

