import csv
import tkinter as tk
from tkinter import messagebox


def create_record():
    name = name_entry.get()
    age = age_entry.get()
    with open('database.csv', mode='a') as csv_file:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'name': name, 'age': age})
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Record created.")


def read_record():
    records = []
    with open('database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            records.append(row)
    if not records:
        messagebox.showerror("Error", "No records found.")
        return
    records_text.configure(state='normal')
    records_text.delete('1.0', tk.END)
    for record in records:
        records_text.insert(tk.END, record)
    records_text.configure(state='disabled')


def update_record():
    name = name_entry.get()
    age = age_entry.get()
    records = []
    found = False
    with open('database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['name'] == name:
                row['age'] = age
                found = True
            records.append(row)
    if not found:
        messagebox.showerror("Error", "Record not found.")
        return
    with open('database.csv', mode='w') as csv_file:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Record updated.")


def delete_record():
    name = name_entry.get()
    records = []
    found = False
    with open('database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['name'] != name:
                records.append(row)
            else:
                found = True
    if not found:
        messagebox.showerror("Error", "Record not found.")
        return
    with open('database.csv', mode='w') as csv_file:
        fieldnames = ['name', 'age']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Record deleted.")


def search_record():
    name = name_entry.get()
    with open('database.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['name'] == name:
                age_entry.delete(0, tk.END)
                age_entry.insert(0, row['age'])
                messagebox.showinfo("Success", "Record found.")
                return
        messagebox.showerror("Error", "Record not found.")
