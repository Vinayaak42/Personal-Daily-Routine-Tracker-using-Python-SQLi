import sqlite3

def connect():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , earnings integer ,excercize text , study text , diet text , expense integer)")
    conn.commit()
    conn.close()

def insert(date,earnings,excercize,study,diet,expense):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)",(date,earnings,excercize,study,diet,expense))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return(rows)

def delete(id):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(date='',earnings='',excercize='',study='',diet='',expense=''):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR earnings=? OR excercize=? OR study=? OR diet=? OR expense=?" , (date , earnings , excercize , study , diet , expense))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return(rows)


# insert('2-3-20',200,'done','done','yes',300)
# insert('2-3-20',400,'done','done','yes',500)
# insert('2-3-20',600,'done','done','yes',700)
# insert('2-3-20',800,'done','done','yes',900)
# print(search(earnings=400))
