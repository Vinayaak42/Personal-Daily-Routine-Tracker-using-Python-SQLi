from tkinter import *
import sqlite3

# ---------- BACKEND FUNCTIONS ----------
def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS routine (
                    Id INTEGER PRIMARY KEY,
                    date TEXT,
                    earnings INTEGER,
                    excercize TEXT,
                    study TEXT,
                    diet TEXT,
                    expense INTEGER)''')
    conn.commit()
    conn.close()

def insert(date, earnings, excercize, study, diet, expense):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                (date, earnings, excercize, study, diet, expense))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search(date='', earnings='', excercize='', study='', diet='', expense=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM routine WHERE 
                    date=? OR earnings=? OR excercize=? OR 
                    study=? OR diet=? OR expense=?''',
                (date, earnings, excercize, study, diet, expense))
    rows = cur.fetchall()
    conn.close()
    return rows

# Ensure database is created
connect()

# ---------- FRONTEND GUI ----------
def selected(event):
    global selected_row
    try:
        index = listbox.curselection()[0]
        selected_row = listbox.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        e5.delete(0, END)
        e5.insert(END, selected_row[5])
        e6.delete(0, END)
        e6.insert(END, selected_row[6])
    except IndexError:
        pass

def delete_cmd():
    if selected_row:
        delete(selected_row[0])
        view_cmd()

def view_cmd():
    listbox.delete(0, END)
    for row in view():
        listbox.insert(END, row)

def search_cmd():
    listbox.delete(0, END)
    for row in search(date_text.get(), earning_text.get(), excercise_text.get(),
                      study_text.get(), diet_text.get(), expense_text.get()):
        listbox.insert(END, row)

def add_cmd():
    insert(date_text.get(), earning_text.get(), excercise_text.get(),
           study_text.get(), diet_text.get(), expense_text.get())
    view_cmd()

win = Tk()
win.wm_title("Daily Routine Tracker")

# Labels
labels = ["Date", "Earnings", "Exercise", "Study", "Diet", "Expenses"]
for idx, text in enumerate(labels):
    Label(win, text=text, bg="#F3F4F6", fg="dark orange", font="Lato 12",
          borderwidth=2, relief="groove", padx=4, pady=4).grid(row=idx//2, column=(idx % 2)*2, sticky=N+S+E+W)

# Entry fields
date_text, earning_text, excercise_text = StringVar(), StringVar(), StringVar()
study_text, diet_text, expense_text = StringVar(), StringVar(), StringVar()

e1 = Entry(win, textvariable=date_text); e1.grid(row=0, column=1)
e2 = Entry(win, textvariable=earning_text); e2.grid(row=0, column=3)
e3 = Entry(win, textvariable=excercise_text); e3.grid(row=1, column=1)
e4 = Entry(win, textvariable=study_text); e4.grid(row=1, column=3)
e5 = Entry(win, textvariable=diet_text); e5.grid(row=2, column=1)
e6 = Entry(win, textvariable=expense_text); e6.grid(row=2, column=3)

# Listbox and Scrollbar
listbox = Listbox(win, height=10, width=40)
listbox.grid(row=3, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=6)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', selected)

# Buttons
buttons = [("ADD", add_cmd), ("SEARCH", search_cmd), ("DELETE", delete_cmd),
           ("VIEW", view_cmd), ("CLOSE", win.destroy)]

for idx, (text, cmd) in enumerate(buttons):
    Button(win, text=text, width=12, pady=5, command=cmd,
           bg="white", fg="blue", font="Lato 12", borderwidth=2,
           relief="groove").grid(row=3 + idx, column=3)

win.mainloop()
