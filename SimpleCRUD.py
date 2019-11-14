
import sqlite3
def DisplayRecords():
    db=sqlite3.connect('test.db')
    sql="SELECT * from student;"
    cur=db.cursor()
    cur.execute(sql)
    while True:
        record=cur.fetchone()
        if record==None:
            break
        print (record)
    db.close()


#insert records in the table
db=sqlite3.connect('test.db')
qry="insert into student (name, age, marks) values(?,?,?);"
students=[('Amar', 18, 70), ('Deepak', 25, 87)]
try:
    cur=db.cursor()
    cur.executemany(qry, students)
    db.commit()
    DisplayRecords()
    print ("records added successfully")
except:
    print ("error in operation")
    db.rollback()
    db.close()


