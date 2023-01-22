import csv
from tkinter import *

root = Tk()
root.title("Motorcycle CRUD App")

# Create a list to store motorcycle data
motorcycles = []

# Function to load data from CSV file


def load_data():
    with open('motor.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            motorcycles.append(row)

# Function to save data to CSV file


def save_data():
    with open('motor.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(motorcycles)

# Function to add a motorcycle


def add_motorcycle():
    make = make_entry.get()
    model = model_entry.get()
    year = year_entry.get()
    color = color_entry.get()
    motorcycle = [make, model, year, color]
    motorcycles.append(motorcycle)
    listbox.insert(END, motorcycle)
    make_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)
    save_data()

# Function to update a motorcycle


def update_motorcycle():
    selected_index = listbox.curselection()[0]
    motorcycles[selected_index][0] = make_entry.get()
    motorcycles[selected_index][1] = model_entry.get()
    motorcycles[selected_index][2] = year_entry.get()
    motorcycles[selected_index][3] = color_entry.get()
    listbox.delete(ACTIVE)
    listbox.insert(selected_index, motorcycles[selected_index])
    make_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)
    save_data()

# Function to delete a motorcycle


def delete_motorcycle():
    selected_index = listbox.curselection()[0]
    del motorcycles[selected_index]
    listbox.delete(ACTIVE)
    save_data()

# Function to display selected motorcycle in the input fields


def select_motorcycle(event):
    selected_index = listbox.curselection()[0]
    selected_item = motorcycles[selected_index]
    make_entry.delete(0, END)
    make_entry.insert(0, selected_item[0])
    model_entry.delete(0, END)
    model_entry.insert(0, selected_item[1])
    year_entry.delete(0, END)
    year_entry.insert(0, selected_item[2])
    color_entry.delete(0, END)
    color_entry.insert(0, selected_item[3])

# Function to clear the input fields


def clear_input():
    make_entry.delete(0, END)
    model_entry.delete(0, END)
    year_entry.delete(0, END)
    color_entry.delete(0, END)


# Create labels for input fields
make_label = Label(root, text="Make")
make_label.grid(row=0, column=0, padx=5, pady=5)
model_label = Label(root, text="Model")
model_label.grid(row=1, column=0, padx=5, pady=5)
year_label = Label(root, text="Year")
year_label.grid(row=2, column=0, padx=5, pady=5)
color_label = Label(root, text="Color")
color_label.grid(row=3, column=0, padx=5, pady=5)

# Create input fields
make_entry = Entry(root)
make_entry.grid(row=0, column=1, padx=5, pady=5)
model_entry = Entry(root)
model_entry.grid(row=1, column=1, padx=5, pady=5)
year_entry = Entry(root)
year_entry.grid(row=2, column=1, padx=5, pady=5)
color_entry = Entry(root)
color_entry.grid(row=3, column=1, padx=5, pady=5)

# Create a Listbox to display motorcycle data
listbox = Listbox(root)
listbox.grid(row=0, column=2, rowspan=6, padx=5, pady=5)
listbox.bind('<<ListboxSelect>>', select_motorcycle)

# Create buttons for CRUD actions
add_button = Button(root, text="Add", command=add_motorcycle)
add_button.grid(row=4, column=0, padx=5, pady=5)
update_button = Button(root, text="Update", command=update_motorcycle)
update_button.grid(row=4, column=1, padx=5, pady=5)
delete_button = Button(root, text="Delete", command=delete_motorcycle)
delete_button.grid(row=4, column=2, padx=5, pady=5)
clear_button = Button(root, text="Clear", command=clear_input)
clear_button.grid(row=5, column=0, padx=5, pady=5)

# Load data from CSV file
load_data()

# Insert data into the Listbox
for motorcycle in motorcycles:
    listbox.insert(END, motorcycle)

root.mainloop()
