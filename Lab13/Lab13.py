#4.	Определить количество взрослых(=>18) и детей(<18)  d 1,2 и 3 классе на борту и сколько из них выжило
import csv

file = open("titanic.csv", "r")
reader = list(csv.reader(file))

det = []
vzros = []
for i in reader:
    if i[0] == "1":
        if i[1] == "1" or i[1] == "2" or i[1] == "3":
            if float(i[4]) < 18.0:
                det.append([i[4]])
            else:
                vzros.append([i[4]])

print(f"Детей выжило:", len(det))
print(f"Взрослых выжило:", len(vzros))
