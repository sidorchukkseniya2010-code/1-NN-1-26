# Простая задача While30
a = float(input("Введите сторону прямоугольника A: "))
b = float(input("Введите сторону прямоугольника B: "))
c = float(input("Введите сторону квадрата C: "))
ostatok_a = a
kolichestvo_po_a = 0
while ostatok_a >= c:
    ostatok_a = ostatok_a - c
    kolichestvo_po_a = kolichestvo_po_a + 1
ostatok_b = b
kolichestvo_po_b = 0
while ostatok_b >= c:
    ostatok_b = ostatok_b - c
    kolichestvo_po_b = kolichestvo_po_b + 1
vsego_kvadratov = kolichestvo_po_a * kolichestvo_po_b
print("Всего квадратов поместилось:", vsego_kvadratov)