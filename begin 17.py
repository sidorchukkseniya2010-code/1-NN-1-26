A=int(input("Введите точку А : "))
B=int(input("Введите точку B : "))
C=int(input("Введите точку C : "))

AC = abs(A-C)
BC = abs(B-C)
AC_BC = AC + BC
AB = abs(A-B)
print("AC: ", AC)
print("BC: ", BC)
print("AC + BC: ", AC_BC)
print("AB: ", AB)
