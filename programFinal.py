import csv
import os
from prettytable import PrettyTable
from stack import Stack
from queueFinal import Queue
from treeFinal import Tree

buah1 = "jeruk"
buah2 = "apel"
harga1 = 10000
harga2 = 14000
hargabeli1 = 5000
hargabeli2 = 7000
hargabeli3 = 100

kemasan = "kardus"
# print("Masukkan barang yang Anda jual: ")
# buah1 = input("masukkan buah 1: ")
# buah2 = input("masukkan buah 2: ")
# harga1 = int(input(f"harga jual {buah1}: "))
# harga2 = int(input(f"harga jual {buah2}: "))
# hargabeli1 = int(input(f"harga beli {buah1}: "))
# hargabeli2 = int(input(f"harga beli {buah2}: "))
# hargabeli3 = int(input("harga beli kardus: "))

totalpembelian = 0
totalpenjualan = 0


s = Stack()
q1 = Queue()
q2 = Queue()
t1 = Tree(buah1)
t2 = Tree(buah2)
t3 = Tree(kemasan)


# nambah cabang perusahaan
def gabung(perusahaan, nama, jenis, value):
    if jenis == buah1:
        if Tree(perusahaan) in t1.children:
            for i in t1.children:
                if Tree(nama) not in i.children:
                    if i == Tree(perusahaan):
                        i.add_child(Tree(nama))
                        t1.add_value(nama, value)
                    else:
                        t1.add_value(nama, value)
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t1.add_child(x)
    elif jenis == buah2:
        if Tree(perusahaan) in t2.children:
            for i in t2.children:
                if Tree(nama) not in i.children:
                    if i == Tree(perusahaan):
                        i.add_child(Tree(nama))
                        t2.add_value(nama, value)
                    else:
                        t2.add_value(nama, value)
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t2.add_child(x)
    elif jenis == kemasan:
        if Tree(perusahaan) in t3.children:
            for i in t3.children:
                if Tree(nama) not in i.children:
                    if i == Tree(perusahaan):
                        i.add_child(Tree(nama))
                        t3.add_value(nama, value)
                    else:
                        t3.add_value(nama, value)
        else:
            x = Tree(perusahaan)
            y = Tree(nama, value)
            x.add_child(y)
            t3.add_child(x)


# apabila ada barang masuk
def barang_masuk(perusahaan, nama, jenis, value):
    gabung(perusahaan, nama, jenis, value)
    masuk_csv(perusahaan, nama, jenis, value)
    if jenis == buah1:
        q1.enqueue(value)
    elif jenis == buah2:
        q2.enqueue(value)
    elif jenis == kemasan:
        s.push(value)
    else:
        print("Jenis barang yang Anda masukkan salah")


def masuk_csv(perusahaan, nama, jenis, value):
    with open('catatan_barang_masuk.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([perusahaan, nama, jenis, value])

# apabila ada barang keluar


def barang_keluar(jenis, barang):
    if jenis == buah1:
        if (sum(s.items)) >= barang/2 and sum(q1.items) >= barang:
            q1.dequeue(barang)
            s.pop(int(barang/2))
            keluar_csv(jenis, barang)
        else:
            print("pengiriman gagal")
    elif jenis == buah2:
        if (sum(s.items)) >= barang/5 and sum(q2.items) >= barang:
            q2.dequeue(barang)
            s.pop(int(barang/5))
            keluar_csv(jenis, barang)
        else:
            print("Pengiriman gagal")
    else:
        print("Jenis barang yang Anda masukkan salah")


def keluar_csv(jenis, barang):
    with open('catatan_barang_keluar.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jenis, barang])


def pembelian():
    table = PrettyTable()
    table.field_names = ["Perusahaan", "Barang",
                         "Harga", "Jumlah", "Harga Beli"]
    # Menambahkan baris data ke tabel t1
    global totalpembelian
    t1list = []
    t2list = []
    t3list = []

    for child in t1.children:
        nama_perusahaan = str(child)
        value = child.calculate_value()
        harga_beli = value * hargabeli2
        table.add_row([nama_perusahaan, buah1, hargabeli1, value, harga_beli])
        t1list.append(value)

    # Menambahkan baris data ke tabel t2
    for child in t2.children:
        nama_perusahaan = str(child)
        value = child.calculate_value()
        harga_beli = value * hargabeli2
        table.add_row([nama_perusahaan, buah2, hargabeli2, value, harga_beli])
        t2list.append(value)

    # Menambahkan baris data ke tabel t3
    for child in t3.children:
        nama_perusahaan = str(child)
        value = child.calculate_value()
        harga_beli = value * hargabeli3
        table.add_row([nama_perusahaan, kemasan,
                      hargabeli3, value, harga_beli])
        t3list.append(value)

    total_harga_beli_t1 = sum(t1list)*hargabeli1
    total_harga_beli_t2 = sum(t2list)*hargabeli2
    total_harga_beli_t3 = sum(t3list)*hargabeli3

    totalpembelian = total_harga_beli_t1 + total_harga_beli_t2 + total_harga_beli_t3

    # Menambahkan total pembelian ke tabel
    table.add_row(["Total Pembelian", "", "", "", totalpembelian])

    print("----------------------------------------------------------")
    print("|                     Total Pembelian                    |")
    print("----------------------------------------------------------")
    # Mencetak tabel
    print(table)


def penjualan():
    # Membuat tabel
    global totalpenjualan
    table = PrettyTable()
    table.field_names = ["Barang", "Jumlah", "Harga", "Harga Jual"]

    # Mengisi data ke tabel
    total1 = q1.penjualan * harga1
    total2 = q2.penjualan * harga2
    totalpenjualan = total1 + total2
    table.add_row([buah1, q1.penjualan, harga1, total1])
    table.add_row([buah2, q2.penjualan, harga2, total2])
    table.add_row(["Total Penjualan", "", "", totalpenjualan])

    print("-------------------------------------------------")
    print("|               Total Penjualan                 |")
    print("-------------------------------------------------")
    print(table)


def persediaan():
    print("--------------------------------------------------------")
    print("|            Persediaan Barang di Gudang               |")
    print("--------------------------------------------------------")
    table = PrettyTable()
    table.field_names = ["Gudang", "Persediaan", "Total Persediaan"]

    table.add_row([buah1, q1.items, q1.total()])
    table.add_row([buah2, q2.items, q2.total()])
    table.add_row([kemasan, s.items, s.total()])

    print(table)


def laporan():
    print("----------------------------------------")
    print("|          Pendapatan Bersih           |")
    print("----------------------------------------")
    table = PrettyTable()
    table.field_names = ["Keterangan", "Total"]

    table.add_row(["Penjualan", totalpenjualan])
    table.add_row(["Pembelian", totalpembelian])
    table.add_row(["Pendapatan Bersih", (totalpenjualan-totalpembelian)])

    print(table)


# Membaca data dari file CSV
with open('data_barang_masuk.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    # Melakukan looping untuk setiap baris data
    for row in reader:
        perusahaan = row[0]
        nama = row[1]
        barang = row[2]
        jumlah = int(row[3])

        # Memanggil fungsi barang_masuk dengan nilai-nilai dari setiap baris
        barang_masuk(perusahaan, nama, barang, jumlah)

with open('data_barang_keluar.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Membaca header
    # Melakukan looping untuk setiap baris data
    for row in reader:
        jenis = row[0]
        jumlah = int(row[1])

        # Memanggil fungsi barang_masuk dengan nilai-nilai dari setiap baris
        barang_keluar(jenis, jumlah)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~                               .''.   ~")
print("~   /\  ()  WELCOME TO FRUSTO   '..'/\ ~")
print("~  .''..''.  ADMINISTRATION        .''.~")
print("~  '..''..'                        '..'~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("----------------------------------------")
print("-         PILIH MENU BERIKUT INI:      -")
print("----------------------------------------")
print(": 1. Daftar Menu:                      :")
print(": 2. Memasukkan Barang:                :")
print(": 3. Mengirim Barang:                  :")
print(": 4. Riwayat Suplier:                  :")
print(": 5. Mengecek Persediaan:              :")
print(": 6. Total Penjualan:                  :")
print(": 7. Total Pembelian:                  :")
print(": 8. Pendapatan Bersih:                :")
print("----------------------------------------")
print()

while True:
    # a,b,c,d = input("nih").split()
    # barang_masuk(a,b,c,int(d))
    n = input("Masukkan pilihan (atau tekan 'q' untuk keluar): ")
    if n == '1':
        print()
        print("---------DAFTAR MENU---------")
        print("-2.Memasukkan Barang        -")
        print("-3.Mengirim Barang          -")
        print("-4.Riwayat Suplier          -")
        print("-5.Mengecek Persediaan      -")
        print("-6.Total Penjualan          -")
        print("-7.Total Pembelian          -")
        print("-8.Pendapatan Bersih        -")
        print("-----------------------------")
        print()
    elif n == '2':
        os.system('clear')
        print("riwayat supplier: ")
        t1.print_tree()
        t2.print_tree()
        t3.print_tree()
        w, x, y, z = input(
            "Masukkan: perusahaan, nama, jenis barang, value: ").split(" ")
        barang_masuk(w, x, y, int(z))
    elif n == "3":
        os.system('clear')
        persediaan()
        x, y = input("Masukkan jenis barang, value : ").split(" ")
        barang_keluar(x, int(y))
    elif n == '4':
        os.system('clear')
        print("----------------------------------------")
        print("|           Riwayat Suplier            |")
        print("----------------------------------------")
        t1.calculate_value()
        t2.calculate_value()
        t3.calculate_value()
        t1.print_tree()
        t2.print_tree()
        t3.print_tree()
        print("________________________________________")
        print()
    elif n == '5':
        os.system('clear')
        persediaan()
        print("________________________________________")
        print()
    elif n == '6':
        os.system('clear')
        penjualan()
        print("_________________________________________________")
        print()
    elif n == '7':
        os.system('clear')
        t1.calculate_value()
        t2.calculate_value()
        t3.calculate_value()
        pembelian()
        print("__________________________________________________________")
        print()
    elif n == "8":
        os.system('clear')
        # jalanin 6 dan 7 dulu buat dapet nilai totalpenjualan dan totalpembelian
        laporan()
    elif n.lower() == 'q':
        print("----------------------------------------")
        print("|            PROGRAM SELESAI            |")
        print("----------------------------------------")
        break
