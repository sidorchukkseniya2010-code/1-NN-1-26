a= int(input("Введите a"))
b= int(input("Введите b"))
count=0
for i in range(a-1,b,-1):
    count +=1
    print(i)
print(f"Количество:{count}")
