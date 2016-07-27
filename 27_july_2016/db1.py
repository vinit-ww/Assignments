import psycopg2
import os
class Postgress(object):
     a=[]
             
     def connection(self):
        conn=psycopg2.connect(database="test1",user="postgres",password="test",host="127.0.0.1",port="5432")
        print "opened database successfully"
        conn.commit()
        return conn
     
     def create_table(self,conn):
        cur = conn.cursor()
        cur.execute('''create table categories(id INT primary key,name text); ''')
        cur.execute('''create table authors(id INT primary key,authors_name text); ''')
        cur.execute('''create table Books(id INT primary key,names_book text,Isbn INT,author_id INT references authors(id),category_id INT  \                   references categories(id)); ''')
        cur.execute('''create table publications(id INT primary key,publications_name text,author_id INT references authors(id) ); ''')
        print "Table created successfully"
        conn.commit()
     
     def insert_value(self,conn):
        cur=conn.cursor()
        cur.execute("INSERT INTO categories(id,name)VALUES(3,'Non Fiction')")
        cur.execute("INSERT INTO authors(id,authors_name)VALUES(3,'apj abdul kalam')")
        cur.execute("INSERT INTO Books(id,names_book,author_id,category_id)VALUES(3,'story of my life',3,3)")
        cur.execute("INSERT INTO publications(id,publications_name,author_id)VALUES(3,'Bloomsbury',3)")
        conn.commit()
        print "records created succesfully"
     
     def select(self,conn):
        cur=conn.cursor()
        cur.execute("select * from Books")
        rows=cur.fetchall()
        for i in rows:
            j=0
            while(j < 4):
                self.a.append(i[j])
                j+=1    
        print "Operation done successfully"
        #close database
        return self.a
        conn.close()
        
     def write(self,thelist):
        os.path.abspath("")
       # os.makedirs('/home/webwerks1/vineet/27_july_2016/assignment')
        f=open('/home/webwerks1/vineet/27_july_2016/assignment/output.txt', 'w')
        for item in thelist:
            print>>f,item
        f.close()
        return f  
     
        
obj=Postgress()
connect=obj.connection()
#obj.create_table(connect)
#obj.insert_value(connect)
my_list=obj.select(connect)
#obj.write(my_list)

