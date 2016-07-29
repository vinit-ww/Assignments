#db_client.py
import os
import psycopg2
class Post(object):
     
     #creating a connection       
     def connection(self):
        conn=psycopg2.connect(database="test1",user="postgres",password="test",host="127.0.0.1",port="5432")
        print "opened database successfully"
        conn.commit()
        conn.close()
     #creating a table
     def create_table(self,conn):
        cur = conn.cursor()
        cur.execute('''create table categories(id INT primary key,name text); ''')
        cur.execute('''create table authors(id INT primary key,authors_name text); ''')
        cur.execute('''create table Books(id INT primary key,names_book text,Isbn INT,author_id INT references authors(id),category_id INT  \                   references categories(id)); ''')
        cur.execute('''create table publications(id INT primary key,publications_name text,author_id INT references authors(id) ); ''')
        print "Table created successfully"
        conn.commit()

     
obj=Post()
obj.connection()
#obj.create_table(connect)

