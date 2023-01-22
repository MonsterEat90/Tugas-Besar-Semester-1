import csv
import tkinter as tk
from tkinter import messagebox

# Create a new Tkinter app
app = tk.Tk()
app.title("Food and Drink Menu")

# Create a CSV file to store menu items
with open("menu.csv", "a+", newline="") as file:
    writer = csv.writer(file)

# Function to add a new menu item


def add_item():
    item = item_entry.get()
    price = price_entry.get()
    with open("menu.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, price])
    messagebox.showinfo("Success", "Item added to menu.")

# Function to view current menu


def view_menu():
    with open("menu.csv", "r") as file:
        reader = csv.reader(file)
        menu_list = list(reader)
    menu_string = ""
    for item in menu_list:
        menu_string += f"{item[0]}: Rp {item[1]}\n"
    messagebox.showinfo("Menu", menu_string)

# Function to update an existing menu item


def update_item():
    item = item_entry.get()
    price = price_entry.get()
    with open("menu.csv", "r") as file:
        reader = csv.reader(file)
        menu_list = list(reader)
    for i, menu_item in enumerate(menu_list):
        if menu_item[0] == item:
            menu_list[i][1] = price
    with open("menu.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(menu_list)
    messagebox.showinfo("Success", "Item updated.")

# Function to delete a menu item


def delete_item():
    item = item_entry.get()
    with open("menu.csv", "r") as file:
        reader = csv.reader(file)
        menu_list = list(reader)
    for i, menu_item in enumerate(menu_list):
        if menu_item[0] == item:
            del menu_list[i]
    with open("menu.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(menu_list)
    messagebox.showinfo("Success", "Item deleted.")


# Create Tkinter widgets for adding a new menu item
item_label = tk.Label(app, text="Item:")
item_label.grid(row=0, column=0)
item_entry = tk.Entry(app)
item_entry.grid(row=0, column=1)
price_label = tk.Label(app, text="Price:")
price_label.grid(row=1, column=0)
price_entry = tk.Entry(app)
price_entry.grid(row=1, column=1)
add_button = tk.Button(app, text="Add Item", command=add_item)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create Tkinter widgets for viewing, updating, and deleting menu items
view_button = tk.Button(app, text="View Menu", command=view_menu)
view_button.grid(row=3, column=0, columnspan=2, pady=10)
update_button = tk.Button(app, text="Update Item", command=update_item)
update_button.grid(row=4, column=0, columnspan=2, pady=10)
delete_button = tk.Button(app, text="Delete Item", command=delete_item)
delete_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter app
app.mainloop()
