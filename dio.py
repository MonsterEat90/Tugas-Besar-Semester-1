import csv
import os

csv_filename = 'datatoko.csv'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    clear_screen()
    print("=== LIST MENU TOKO HP ===")
    print("[1] Lihat Daftar Barang Toko")
    print("[2] Buat Data Toko Baru")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Cari Data Toko")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")

    if (selected_menu == "1"):
        show_contact()
    elif (selected_menu == "2"):
        create_contact()
    elif (selected_menu == "3"):
        edit_contact()
    elif (selected_menu == "4"):
        delete_contact()
    elif (selected_menu == "5"):
        search_contact()
    elif (selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    if (len(contacts) > 0):
        labels = contacts.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]}")
        print("-"*34)
        for data in contacts:
            print(f'{data[0]} \t {data[1]} \t {data[2]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_contact():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'HARGA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        no = input("No urut: ")
        nama = input("Nama lengkap: ")
        harga = input("Harga : ")

        writer.writerow({'NO': no, 'NAMA': nama, 'HARGA': harga})
        print("Berhasil disimpan!")

    back_to_menu()


def search_contact():
    clear_screen()
    toko = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            toko.append(row)

    no = input("Cari berdasrakan nomer urut> ")

    data_found = []

    # mencari contact
    indeks = 0
    for data in toko:
        if (data['NO'] == no):
            data_found = toko[indeks]

        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Harga: {data_found['HARGA']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()


def edit_contact():
    clear_screen()
    toko = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            toko.append(row)

    print("NO \t NAMA BARANG \t\t HARGA")
    print("-" * 32)

    for data in toko:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['HARGA']}")

    print("-----------------------")
    no = input("Pilih nomer Data> ")
    nama = input("nama baru: ")
    harga = input("harga baru: ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['HARGA'] = harga
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'HARGA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow(
                {'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'HARGA': new_data['HARGA']})

    back_to_menu()


def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t HARGA")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['HARGA']}")

    print("-----------------------")
    no = input("Hapus> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'HARGA']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow(
                {'NO': new_data['NO'], 'NAMA': new_data['NAMA'], 'TELEPON': new_data['HARGA']})

    print("Data sudah terhapus")
    back_to_menu()


if __name__ == "__main__":
    while True:
        show_menu()
