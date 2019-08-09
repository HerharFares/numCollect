import re
import sqlite3
from sqlite3 import Error

'''
this module is used for managing data base connections and every thing related;
this applies for all(in case True that means the query worked False if else)

for all the methods declared below, have one thing in common ::
        True ==> if the methods works fine
        False ==> else

need improvements, so go ahead.  
'''


class Db(object):
    def __init__(self, db):
        self.db = db
        self.conn = ''
        self.query = ''
        self.cur = ''
    

    def connect(self):
        '''
        function used for starting the connection, to
        the data base -db-.
        '''
        try:
            self.conn = sqlite3.Connection(self.db)
            self.cur = self.conn.cursor()
            return True
            
        except Error:
            self.conn.close()
            return False   
        

    def close(self):
        '''
        at the end of what ever you are doing in the DB, use this
        method to close all connections.

        might say the garbage collector will take care, but no
        clean code is way better for both meaning and performance.
        '''
        try:
            self.cur.close()
            self.conn.close()
            return True
        
        except Error:
            return False
            

    def createTable(self, table_query):
        '''
        this functions is made specially for creating tables,
        you can use the other function listed below, but this way i know
        exactly what i am doing.

        table_query == the quey to insert the table

        table = \'''
        CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL
        );
        \'''
        '''
        try:
            self.cur.execute(table_query)
            self.conn.commit()
            return True
        
        except Error as e:
            raise e



    def prepareQuery(self, query):
        '''
        At first, call the method with ::

        quey = INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                      VALUES(?,?,?,?,?,?)

        insert = prepareQuery(query)
        just to prepare the query for doing what ever
            like :: multi inserting elements.

        then call the second method like
        insertRow(list of values by the same order)

        this inner method can be called as many as you need.
        before using any of the methods listed under, you should use this one before.
        '''
        try:
            self.query = query
            return True
        
        except Error:
            return False
        

    def insertRow(self, row):
        '''
        but before using it, use the prepareQuery(), then call this
        one with a list of the parameters(Values).

        as said for inserting multiple data rows.
        
        Ex:
        ---
        prepareQuery(query)
        insertRow([data1, data2, ...........])
        '''
        try:
            self.cur.execute(self.query, row)
            self.conn.commit()
            return True

        except Error as e:
            print(e)


    def justQuery(self, row=None):
        '''
        but before using it, use the prepareQuery(), then call this
        one with a list of the parameters(Values).

        for another usage query like delete, update any other type for queries
        that does not have anything as an output on.
        
        Ex:
        ---
        query = ALTER TABLE [YOUR TABLE]
                SET [COLMUN1]=  ? -VALUE1-
                WHERE [COLOMUN2]=? -VALUE2-

        prepareQuery(query)
        insertRow([data1, data2])
        '''

        try:
            if row == None:
                self.cur.execute(self.query)
            else:
                self.cur.execute(self.query, row)

            self.conn.commit()
            return True
        except:
            return False
    

    def extractData(self, data=None):
        '''
        but before using it, use the prepareQuery(), then call this
        one with a list of the parameters(Values).

        for data extraction; but it does not give the rows,
        so you should know them.

        in case it returns None it means that there is something wrong with the query
        or it is just that the query output is empty.

        Ex1:
        ---
        query = SELECT * FROM TABLE [YOUR TABLE]
                WHERE [COLOMUN2]=? -VALUE1-

        prepareQuery(query)
        insertRow([data1])


        Ex2:
        ---
        query = SELECT * FROM TABLE [YOUR TABLE]

        prepareQuery(query)
        insertRow()
        '''
        try:
            if row != None:
                self.cur.execute(self.query, data)
            else:
                self.cur.execute(self.query)

            for row in self.cur.fetchall():
                yield row

                
        except Error:
            yield None 
    


    def notTableOutPutQuey(self, data=None):
        '''
        but before using it, use the prepareQuery(), then call this
        one with a list of the parameters(Values).

        this is made for -- none table -- output queries
        like:
        select coun(*)
        select max()....
            with out Goup By
        
        in case it returns None it means that there is some thing wrong with the query.
        
        Ex1:
        ----
            query = SELECT count(*) FROM [YOUR TABLE]
            prepareQuery(query)
            notTableOutPutQuery()
        
        Ex2:
        ----
            query = SELECT count(*) FROM [YOUR TABLE]
                    HAVING BY  [COLOMN]=? -VALUE-
            
            prepareQuery(query)
            notTableOutPutQuery([data])

        '''
        try:
            if data != None:
                self.cur.execute(self.query, data)
            else:
                self.cur.execute(self.query)

            d = self.cur.fetchall()[0]
            return d[0]   
                
        except Error:
            return None
        
        
if __name__ == '__main__':
    pass
