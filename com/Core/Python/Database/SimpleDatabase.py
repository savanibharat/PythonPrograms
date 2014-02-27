'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
import sqlite3

def main():
    db = sqlite3.connect("test.db")
    db.row_factory=sqlite3.Row
    db.execute("drop table if exists test")
    db.execute("create table test (t1 text,i1 int)")
    db.execute("insert into test (t1,i1) values (?,?)", ("one", 1))
    db.execute("insert into test (t1,i1) values (?,?)", ("two", 2))
    db.execute("insert into test (t1,i1) values (?,?)", ("three", 3))
    db.execute("insert into test (t1,i1) values (?,?)", ("four", 4))
    db.execute("insert into test (t1,i1) values (?,?)", ("five", 5))
    db.commit()
    cursor = db.execute("select i1,t1 from test order by t1")
    for row in cursor:
        print row
       

if __name__ == '__main__':main()
'''
print row
(5, u'five')
(4, u'four')
(1, u'one')
(3, u'three')
(2, u'two')

print dict(row)
{'i1': 5, 't1': u'five'}
{'i1': 4, 't1': u'four'}
{'i1': 1, 't1': u'one'}
{'i1': 3, 't1': u'three'}
{'i1': 2, 't1': u'two'}

 print row["t1"],row["i1"]
five 5
four 4
one 1
three 3
two 2


'''