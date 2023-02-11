import csv
from tkinter import *

root = Tk()
root.title("Motorcycle CRUD App")

motorcycles = []


def load_data():
    with open('motor.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            motorcycles.append(row)


def save_data():
    with open('motor.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(motorcycles)


def add_motorcycle():
    merk = merk_entry.get()
    model = model_entry.get()
    year = year_entry.get()
    color = color_entry.get()
    motorcycle = [merk, model, year, color]
    motorcycles.append(motorcycle)
    listbox.insert(END, motorcycle)
    merk_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)
    save_data()


def update_motorcycle():
    selected_index = listbox.curselection()[0]
    motorcycles[selected_index][0] = merk_entry.get()
    motorcycles[selected_index][1] = model_entry.get()
    motorcycles[selected_index][2] = year_entry.get()
    motorcycles[selected_index][3] = color_entry.get()
    listbox.delete(ACTIVE)
    listbox.insert(selected_index, motorcycles[selected_index])
    merk_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)
    search()
    save_data()


def delete_motorcycle():
    selected_index = listbox.curselection()[0]
    del motorcycles[selected_index]
    listbox.delete(ACTIVE)
    search()
    save_data()


def select_motorcycle(event):
    selected_index = listbox.curselection()[0]
    selected_item = motorcycles[selected_index]
    merk_entry.delete(0, END)
    merk_entry.insert(0, selected_item[0])
    model_entry.delete(0, END)
    model_entry.insert(0, selected_item[1])
    year_entry.delete(0, END)
    year_entry.insert(0, selected_item[2])
    color_entry.delete(0, END)
    color_entry.insert(0, selected_item[3])


def clear_input():
    merk_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)


def search(event=None):
    search_term = search_entry.get()
    listbox.delete(0, END)
    for motorcycle in motorcycles:
        if search_term.lower() in motorcycle[0].lower() or search_term.lower() in motorcycle[1].lower():
            listbox.insert(END, motorcycle)


# keterangan input
make_label = Label(root, text="Merek")
make_label.grid(row=0, column=0, padx=5, pady=5)
model_label = Label(root, text="Model")
model_label.grid(row=1, column=0, padx=5, pady=5)
year_label = Label(root, text="Tahun")
year_label.grid(row=2, column=0, padx=5, pady=5)
color_label = Label(root, text="Warna")
color_label.grid(row=3, column=0, padx=5, pady=5)

# tempat input
merk_entry = Entry(root)
merk_entry.grid(row=0, column=1, padx=5, pady=5)
model_entry = Entry(root)
model_entry.grid(row=1, column=1, padx=5, pady=5)
year_entry = Entry(root)
year_entry.grid(row=2, column=1, padx=5, pady=5)
color_entry = Entry(root)
color_entry.grid(row=3, column=1, padx=5, pady=5)

# tempat untuk memunculkan data csv
listbox = Listbox(root, width=50, height=20)
listbox.grid(row=0, column=2, rowspan=6, padx=5, pady=5)
listbox.bind('<<ListboxSelect>>', select_motorcycle)

# tombol CDUS
add_button = Button(root, text="Add", command=add_motorcycle)
add_button.grid(row=4, column=0, padx=5, pady=5)
update_button = Button(root, text="Update", command=update_motorcycle)
update_button.grid(row=4, column=1, padx=5, pady=5)
delete_button = Button(root, text="Delete", command=delete_motorcycle)
delete_button.grid(row=5, column=1, padx=5, pady=5)
search_label = Label(root, text="Search")
search_label.grid(row=0, column=3, padx=5, pady=5, sticky=W)
search_entry = Entry(root)
search_entry.grid(row=0, column=4, padx=5, pady=5, sticky=W)
search_entry.bind('<Return>', search)

# menghilangkan tulisan pada input fields
clear_button = Button(root, text="Clear", command=clear_input)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Load data
load_data()

# membaca data dari csv
for motorcycle in motorcycles:
    listbox.insert(END, motorcycle)

root.mainloop()
