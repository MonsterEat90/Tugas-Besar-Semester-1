import csv
import os

csv_filename = 'datatokoku.csv'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    clear_screen()
    print("=== LIST DATA TOKO ===")
    print("[1] Lihat Daftar Barang")
    print("[2] Buat Data Baru")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Cari Data Barang")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu > ")

    if (selected_menu == "1"):
        show_data()
    elif (selected_menu == "2"):
        create_data()
    # elif (selected_menu == "3"):
    #     edit_data()
    # elif (selected_menu == "4"):
    #     delete_data()
    # elif (selected_menu == "5"):
    #     search_data()
    elif (selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_data():
    clear_screen()
    databarang = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            databarang.append(row)

    if (len(databarang) > 0):
        labels = databarang.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for databarang in databarang:
            print(f'{databarang[0]} \t {databarang[1]} \t {databarang[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_data():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'TELEPON']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        no = input("No urut: ")
        nama = input("Nama lengkap: ")
        telepon = input("No. Telepon: ")

        writer.writerow({'NO': no, 'NAMA': nama, 'TELEPON': telepon})
        print("Berhasil disimpan!")

    back_to_menu()


show_menu()
