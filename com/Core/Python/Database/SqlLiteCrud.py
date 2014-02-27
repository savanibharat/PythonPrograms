'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
import sqlite3

def insert(db, row):
    db.execute("insert into mydb (t1,i1) values (?,?)", (row["t1"], row["i1"]))
    db.commit()
    
def retrive(db, t1):
    cursor = db.execute("select * from mydb where t1=?", (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute("update mydb set i1=? where t1=?", (row["i1"], row["t1"]))
    db.commit()

def delete(db, t1):
    db.execute("delete from mydb where t1=?", (t1,))
    db.commit()
    
def display_rows(db):
    cursor = db.execute("select * from mydb order by t1")
    for row in cursor:
        print("     {}: {}".format(row["t1"], row["i1"]))
        
def main():
    db = sqlite3.connect("mydb.db")
    db.row_factory = sqlite3.Row
    print("Create table mydb.db")
    db.execute("drop table if exists mydb")
    db.execute("create table mydb (t1 text,i1 int)")
    
    print("Create Rows")
    insert(db, dict(t1="one", i1=1))
    insert(db, dict(t1="two", i1=2))
    insert(db, dict(t1="three", i1=3))
    insert(db, dict(t1="four", i1=4))
    display_rows(db)
    
    print("Retrive Rows")
    print(dict(retrive(db, 'one')), dict(retrive(db, 'two')))
    
    print("Update Rows")
    update(db, dict(t1='one', i1=101))
    update(db, dict(t1='three', i1=103))
    display_rows(db)
    
    print("Delete Rows")
    delete(db, 'one')
    delete(db, 'three')
    display_rows(db)
    
if __name__ == '__main__':main()
'''
Create table mydb.db
Create Rows
     four: 4
     one: 1
     three: 3
     two: 2
Retrive Rows
({'i1': 1, 't1': u'one'}, {'i1': 2, 't1': u'two'})
Update Rows
     four: 4
     one: 101
     three: 103
     two: 2
Delete Rows
     four: 4
     two: 2


'''