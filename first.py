import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
import csv

# ----------------- Database Setup ----------------- #
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
''')
conn.commit()

# ----------------- Functions ----------------- #
def add_student():
    name = entry_name.get()
    if name:
        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        messagebox.showinfo("Success", f"Student '{name}' added.")
        entry_name.delete(0, tk.END)
        refresh_students()
    else:
        messagebox.showwarning("Input Error", "Please enter student name.")

def mark_attendance():
    student = selected_student.get()
    status = selected_status.get()
    date = entry_date.get()

    if student and status and date:
        student_id = student_dict[student]
        cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                       (student_id, date, status))
        conn.commit()
        messagebox.showinfo("Success", f"Attendance marked for {student}.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def view_attendance():
    top = tk.Toplevel(root)
    top.title("Attendance Records")

    tree = ttk.Treeview(top, columns=("Name", "Date", "Status"), show='headings')
    tree.heading("Name", text="Name")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.pack(fill=tk.BOTH, expand=True)

    cursor.execute('''
        SELECT students.name, attendance.date, attendance.status 
        FROM attendance
        JOIN students ON students.student_id = attendance.student_id
    ''')
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

def filter_attendance(from_date, to_date):
    top = tk.Toplevel(root)
    top.title(f"Attendance from {from_date} to {to_date}")

    tree = ttk.Treeview(top, columns=("Name", "Date", "Status"), show='headings')
    tree.heading("Name", text="Name")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.pack(fill=tk.BOTH, expand=True)

    cursor.execute('''
        SELECT students.name, attendance.date, attendance.status 
        FROM attendance
        JOIN students ON students.student_id = attendance.student_id
        WHERE date BETWEEN ? AND ?
    ''', (from_date, to_date))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

def export_to_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        cursor.execute('''
            SELECT students.name, attendance.date, attendance.status 
            FROM attendance
            JOIN students ON students.student_id = attendance.student_id
        ''')
        rows = cursor.fetchall()

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
            writer.writerows(rows)

        messagebox.showinfo("Exported", f"Data exported to {file_path}")

def refresh_students():
    global student_dict
    student_dict.clear()
    selected_student.set("")
    student_menu['menu'].delete(0, 'end')
    cursor.execute("SELECT student_id, name FROM students")
    for sid, name in cursor.fetchall():
        student_dict[name] = sid
        student_menu['menu'].add_command(label=name, command=tk._setit(selected_student, name))

# ----------------- GUI ----------------- #
root = tk.Tk()
root.title("Student Attendance Tracker")
root.geometry("550x500")

student_dict = {}

# Add Student Section
frame_add = tk.LabelFrame(root, text="Add Student", padx=10, pady=10)
frame_add.pack(fill="x", padx=10, pady=5)

tk.Label(frame_add, text="Name:").pack(side="left")
entry_name = tk.Entry(frame_add)
entry_name.pack(side="left", padx=5)
tk.Button(frame_add, text="Add", command=add_student).pack(side="left", padx=5)

# Attendance Section
frame_attend = tk.LabelFrame(root, text="Mark Attendance", padx=10, pady=10)
frame_attend.pack(fill="x", padx=10, pady=5)

selected_student = tk.StringVar()
student_menu = tk.OptionMenu(frame_attend, selected_student, "")
student_menu.pack(side="left", padx=5)

selected_status = tk.StringVar(value="Present")
status_menu = tk.OptionMenu(frame_attend, selected_status, "Present", "Absent")
status_menu.pack(side="left", padx=5)

entry_date = tk.Entry(frame_attend)
entry_date.insert(0, "YYYY-MM-DD")
entry_date.pack(side="left", padx=5)

tk.Button(frame_attend, text="Mark", command=mark_attendance).pack(side="left", padx=5)

# Date Filter Section
frame_filter = tk.LabelFrame(root, text="Filter Attendance by Date", padx=10, pady=10)
frame_filter.pack(fill="x", padx=10, pady=5)

tk.Label(frame_filter, text="From (YYYY-MM-DD):").pack(side="left")
entry_from = tk.Entry(frame_filter, width=12)
entry_from.pack(side="left", padx=5)

tk.Label(frame_filter, text="To:").pack(side="left")
entry_to = tk.Entry(frame_filter, width=12)
entry_to.pack(side="left", padx=5)

tk.Button(frame_filter, text="Filter", command=lambda: filter_attendance(entry_from.get(), entry_to.get())).pack(side="left", padx=5)

# Action Buttons
tk.Button(root, text="View Attendance Records", command=view_attendance).pack(pady=10)
tk.Button(root, text="Export to CSV", command=export_to_csv).pack(pady=5)

refresh_students()
root.mainloop()
