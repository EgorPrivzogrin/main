import math
if __name__ == "__main__":
    a = int(input("Введите коэффициент а: "))
    b = int(input("Введите коэффициент b: "))
    c = int(input("Введите коэффициент c: "))
    D = (b**2)-4*a*c
    if D < 0:
        print("Корней нет")
    elif D == 0:
        x1 = (-b/(2*a))
        print("Корень: "+x1)
    else:
        x1 = ((-1*b+math.sqrt(D))/(2*a))
        x2 = ((-1*b-math.sqrt(D))/(2*a))
        print("Первый корень: "+x1+"; Второй корень: "+x2)
