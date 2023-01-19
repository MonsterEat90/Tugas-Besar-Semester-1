import tkinter as tk
from tkinter import ttk
import pandas as pd

# Read data from CSV file
df = pd.read_csv('rumah.csv')

# Create main window
root = tk.Tk()
root.title("Data Rumah")

create_win = None

# Create a treeview to display data
tree = ttk.Treeview(root)
tree["columns"] = ("alamat", "luas", "harga", "jumlah_kamar",
                   "kamar_mandi", "garasi", "tahun_dibangun", "sertifikat", "fasilitas")
tree.heading("#0", text="ID")
tree.heading("alamat", text="Alamat")
tree.heading("luas", text="Luas")
tree.heading("harga", text="Harga")
tree.heading("jumlah_kamar", text="Jumlah Kamar")
tree.heading("kamar_mandi", text="Jumlah Kamar Mandi")
tree.heading("garasi", text="Garasi")
tree.heading("tahun_dibangun", text="Tahun Dibangun")
tree.heading("sertifikat", text="Sertifikat")
tree.heading("fasilitas", text="Fasilitas")
tree.column("#0", width=50)
tree.column("alamat", width=200)
tree.column("luas", width=100)
tree.column("harga", width=100)
tree.column("jumlah_kamar", width=120)
tree.column("kamar_mandi", width=120)
tree.column("garasi", width=100)
tree.column("tahun_dibangun", width=120)
tree.column("sertifikat", width=120)
tree.column("fasilitas", width=200)
tree.pack()

# Insert data into treeview
for i in range(len(df)):
    tree.insert("", "end", text=str(df.iloc[i]["id"]), values=(df.iloc[i]["alamat"], df.iloc[i]["luas"], df.iloc[i]["harga"], df.iloc[i]["jumlah_kamar"],
                df.iloc[i]["kamar_mandi"], df.iloc[i]["garasi"], df.iloc[i]["tahun_dibangun"], df.iloc[i]["sertifikat"], df.iloc[i]["fasilitas"]))

# Create function for "Create" button


def create_data():
    global create_win
    # Open a new window for user input
    create_win = tk.Toplevel(root)
    create_win.title("Create Data")

    # Create labels and entry fields for input
    alamat_label = tk.Label(create_win, text="Alamat:")
    alamat_label.grid(row=0, column=0)
    alamat_entry = tk.Entry(create_win)
    alamat_entry.grid(row=0, column=1)

    luas_label = tk.Label(create_win, text="Luas:")
    luas_label.grid(row=1, column=0)
    luas_entry = tk.Entry(create_win)
    luas_entry.grid(row=1, column=1)

    harga_label = tk.Label(create_win, text="Harga:")
    harga_label.grid(row=2, column=0)
    harga_entry = tk.Entry(create_win)
    harga_entry.grid(row=2, column=1)

    jumlah_kamar_label = tk.Label(create_win, text="Jumlah Kamar:")
    jumlah_kamar_label.grid(row=3, column=0)
    jumlah_kamar_entry = tk.Entry(create_win)
    jumlah_kamar_entry.grid(row=3, column=1)

    kamar_mandi_label = tk.Label(create_win, text="Jumlah Kamar Mandi:")
    kamar_mandi_label.grid(row=4, column=0)
    kamar_mandi_entry = tk.Entry(create_win)
    kamar_mandi_entry.grid(row=4, column=1)

    garasi_label = tk.Label(create_win, text="Garasi:")
    garasi_label.grid(row=5, column=0)
    garasi_entry = tk.Entry(create_win)
    garasi_entry.grid(row=5, column=1)

    tahun_dibangun_label = tk.Label(create_win, text="Tahun Dibangun:")
    tahun_dibangun_label.grid(row=6, column=0)
    tahun_dibangun_entry = tk.Entry(create_win)
    tahun_dibangun_entry.grid(row=6, column=1)

    sertifikat_label = tk.Label(create_win, text="Sertifikat:")
    sertifikat_label.grid(row=7, column=0)
    sertifikat_entry = tk.Entry(create_win)
    sertifikat_entry.grid(row=7, column=1)

    fasilitas_label = tk.Label(create_win, text="Fasilitas:")
    fasilitas_label.grid(row=8, column=0)
    fasilitas_entry = tk.Entry(create_win)
    fasilitas_entry.grid(row=8, column=1)

    # Create "Save" button
    save_button = tk.Button(create_win, text="Save", command=save_data)
    save_button.grid(row=9, column=1)


def save_data():
    for child in root.children.values():
        if child.winfo_class() == 'Toplevel':
            child.destroy()
    # Get user input
    alamat = tk.Entry(root)
    luas = tk.Entry(root)
    harga = tk.Entry(root)
    jumlah_kamar = tk.Entry(root)
    kamar_mandi = tk.Entry(root)
    garasi = tk.Entry(root)
    tahun_dibangun = tk.Entry(root)
    sertifikat = tk.Entry(root)
    fasilitas = tk.Entry(root)
    # Get the next id value
    next_id = df["id"].max() + 1

    # Append new data to the DataFrame
    df.loc[len(df)] = [next_id, alamat, luas, harga, jumlah_kamar,
                       kamar_mandi, garasi, tahun_dibangun, sertifikat, fasilitas]

    # Save DataFrame to CSV file
    df.to_csv('rumah.csv', index=False)

    # Insert new data into treeview
    tree.insert("", "end", text=str(next_id), values=(alamat, luas, harga,
                jumlah_kamar, kamar_mandi, garasi, tahun_dibangun, sertifikat, fasilitas))

    # Close the create window
    create_win.destroy()


# Create "Create" button
create_button = tk.Button(root, text="Create", command=create_data)
create_button.pack()

# Run main loop
root.mainloop()
