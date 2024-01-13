print("power by:")
print("Umbu Nandar Lakingunju_23083000098")
print("umbulakingudju26@gmail.com")
print("kalkulator")


print("================")
print("1. penjumlahan")
print("2. penngurangan")
print("3. pembagian")
print("4. perkalian")
print("================")

operasi = int(input("Masukan pilihan operasi (1/2/3/4) : "))

if operasi == 1:
    x = int(input("Masukan nilai pertama : "))
    y = int(input("Masukan nilai kedua : "))
    z = x + y
    print("hasilnya adalah : ", x, "+", y, "=", z)
    print("=========================")

if operasi == 2:
    x = int(input("Masukan nilai pertama : "))
    y = int(input("Masukan nilai kedua : "))
    z = x - y
    print("hasilnya adalah : ", x, "-", y, "=", z)
    print("=========================")

if operasi == 3:
    x = float(input("Masukan nilai pertama : "))
    y = float(input("Masukan nilai kedua : "))
    z = x / y
    print("hasilnya adalah : ", x, "/", y, "=", z)
    print("=========================")

if operasi == 4:
    x = int(input("Masukan nilai pertama : "))
    y = int(input("Masukan nilai kedua : "))
    z = x * y
    print("hasilnya adalah : ", x, "x", y, "=", z)
    print("=========================")
    