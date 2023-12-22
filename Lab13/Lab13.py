#4.	Определить количество взрослых(=>18) и детей(<18)  d 1,2 и 3 классе на борту и сколько из них выжило
import csv

file = open("titanic.csv", "r")
reader = list(csv.reader(file))

det1 = []
vzros1 = []
det2 = []
vzros2 = []
det3 = []
vzros3 = []
for i in reader:
    if i[0] == "1":
        if i[1] == "1":
            if float(i[4]) < 18.0:
                det1.append([i[4]])
            else:
                vzros1.append([i[4]])
        if i[1] == "2":
            if float(i[4]) < 18.0:
                det2.append([i[4]])
            else:
                vzros2.append([i[4]])
        if i[1] == "3":
            if float(i[4]) < 18.0:
                det3.append([i[4]])
            else:
                vzros3.append([i[4]])
print("Выжившие в первом классе")
print(f"Дети:", len(det1))
print(f"Взрослые:", len(vzros1))
print("Выжившие во втором классе")
print(f"Дети:", len(det2))
print(f"Взрослые:", len(vzros2))
print("Выжившие в третьем классе")
print(f"Дети:", len(det3))
print(f"Взрослые:", len(vzros3))
