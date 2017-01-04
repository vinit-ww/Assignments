import psycopg2
class Postgress(object):
    def connection(self,database_name,user_name,password_name):
        conn=psycopg2.connect(database=database_name,user=user_name,password=password_name,host="127.0.0.1",port="5432")
        print "opened database successfully"
        conn.commit()
        return conn
    def create_table(self,conn):
        cur = conn.cursor()
        cur.execute('''create table Books(roll_no text,Fiction text,NonFiction text,Biography text); ''')
        print "Table created successfully"
        conn.commit()
        
    def insert(self,conn,my_List):
        cur=conn.cursor()
        cur.execute("insert into Books(roll_no,Fiction,NonFiction,Biography) values (%s,%s,%s,%s)",my_List)   
        #save changes
        conn.commit()
        
    def select(self,conn):
        cur=conn.cursor()
        cur.execute("select * from Books")
        rows=cur.fetchall()
        for i in rows:
            print i
        print "Operation done successfully"
        #close database
        conn.close()
       
   
obj=Postgress()
connect=obj.connection("postgres","postgres","test")

#print "Do you want to create table 1 or 0"
#value=raw_input("<<")


#obj.create_table(connect)
a=[]
b=raw_input('Enter values Id value')
a.append(b)    
b=raw_input('Enter values first value')
a.append(b)    
b=raw_input('Enter values second value')
a.append(b)    
b=raw_input('Enter values third value')
a.append(b)
#obj.insert(connect,a)
obj.select(connect)

