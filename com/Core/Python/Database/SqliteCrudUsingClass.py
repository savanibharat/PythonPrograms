'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
import sqlite3
class database:
    def __init__(self,**kwargs):
        self.filename=kwargs.get("filename")
        self.table=kwargs.get('table','newtable')
        
    def sql_do(self,sql,*params):
        self._db.execute(sql,params)
        self._db.commit()
        
    def insert(self,row):
        self._db.execute('insert into {} (t1,i1) values (?,?)'.format(self._table),(row['t1'],row['i1']))
        self._db.commit()
    
    def retrive(self,key):
        cursor=self._db.execute("select * from {} where t1=?".format(self._table),(key,))
        return dict(cursor.fetchone())
    
    def update(self,row):
        self._db.execute("update {} set i1=? where t1=?".format(self._table),(row['i1'],row['t1']))
        self._db.commit()
        
    def delete(self,key):
        self._db.execute('delete from {} where t1=?'.format(self._table,(key,)))
        self._db.coomit()
        
    def display_rows(self):
        cursor=self._db.execute("select * from {} order by t1".format(self._table))
        for row in cursor:
            print ("   {} : {}".format(row["t1"],row["i1"]))
            
    def __iter__(self):
        cursor=self._db.execute("select * from {} order by t1".format(self._table))
        for row in cursor:
            yield dict(row)
            
    @property
    def filename(self): 
        return self._filename
    
    @filename.setter
    def filename(self,fn):
        self._filename=fn
        self._db=sqlite3.connect(fn)
        self._db.row_factory=sqlite3.Row
    @filename.deleter
    def filename(self):
        self.close()
        
    @property
    def table(self):
        return self._table
    @table.setter
    def table(self,t):
        self._table=t
    @table.deleter
    def table(self):
        self._table='newtable'
        
    def close(self):
        self._db.close()
        del self._filename
        
        
def main():

    db=database(filename="newtable.db",table="newtable")
    
    print("Create table newtable")
    db.sql_do("drop table if exists newtable")
    db.sql_do("create table newtable (t1 text,i1 int)")
    
    print("Create rows")
    db.insert(dict(t1="one",i1=1))
    db.insert(dict(t1="two",i1=2))
    db.insert(dict(t1="three",i1=3))
    db.insert(dict(t1="four",i1=4))
    
    for row in db:
        print(row)
    print    
    print("Retrive rows")
    print(db.retrive('one'),db.retrive('two'))
    
    print("Update rows")
    db.update(dict(t1='one',i1=101))
    db.update(dict(t1='three',i1=103))
    for row in db:
        print row
    
    print("Delete rows")
    db.delete('one')
    db.delete('three')
    for row in db:
        print row
        
        
if __name__ == '__main__':main()