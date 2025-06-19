malumotlar = input("malaumotlaringzni kiriting :")
qismLlar = malumotlar.split(',')
for qism in qismLlar:
    juft = qism.strip().split(":")
    print(f"{juft[0]}:{juft[1]}")


