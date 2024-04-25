from random import randint

def mysp(x, n):
    return [x for i in range(n)]

def initsp(a, b, n):
    a = [randint(a, b) for i in range(n)]
    return a

if __name__ == "__main__": 
    # следующий код будет выполняться только при запуске этого файла
    # при импорте этого файла как модуля - выполняться не будет
    n = 100
    b = initsp(1,10,20)
    print(b)

