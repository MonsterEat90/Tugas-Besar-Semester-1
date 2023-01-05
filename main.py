import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("CRUD App")

# Create a list to store the items
items = []

# Create a function to add an item to the list


def add_item():
    # Get the item from the input field
    item = entry.get()

    # Add the item to the list
    items.append(item)

    # Clear the input field
    entry.delete(0, tk.END)

    # Update the list box with the new list
    update_list_box()

# Create a function to delete an item from the list


def delete_item():
    # Get the selected item from the list box
    selected_item = list_box.get(list_box.curselection())

    # Remove the item from the list
    items.remove(selected_item)

    # Update the list box with the new list
    update_list_box()

# Create a function to update the list box


def update_list_box():
    # Clear the list box
    list_box.delete(0, tk.END)

    # Insert each item in the list into the list box
    for item in items:
        list_box.insert(tk.END, item)


# Create an input field and a button to add items to the list
entry = tk.Entry(window)
add_button = tk.Button(window, text="Add", command=add_item)

# Create a list box to display the items in the list
list_box = tk.Listbox(window)

# Create a button to delete items from the list
delete_button = tk.Button(window, text="Delete", command=delete_item)

# Add the widgets to the window
entry.pack()
add_button.pack()
list_box.pack()
delete_button.pack()

# Run the main loop
window.mainloop()
