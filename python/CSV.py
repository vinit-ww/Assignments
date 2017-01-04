import csv
import sqlite3


class Read:
   
   
   def csv_reader(self,file_path):
       """
       read csv file
       
       """
       new_list = []
       
       file_obj=open(file_path,"r")
       
       reader=csv.reader(file_obj)
       
       for row in reader :
           
           new_list.append(row)
           
       return new_list
       
   def insert(self,my_List):
       
       #connecting database 
       conn=sqlite3.connect('myDatabase')
       
       #once we have the connection we can create the cursor object to execute() query
       c = conn.cursor()
       
       #Create table
       c.execute('''CREATE TABLE info( FirstName text ,LastName text ,EmailId text )''')
      
       for t in my_List :
           c.execute("insert into info(FirstName , LastName ,EmailId) values (?,?,?)",(t[0],t[1],t[2],)) 
         
       
       if (c.execute("SELECT * FROM info ")):
           r =c.fetchall()
           for member in r:
               print member
        
      
          
       """       
       #select statement
       
       str1=List[0]
       str2=List[1]
       str3=List[2]
       
       if (c.execute("SELECT * FROM info WHERE FirstName like '%s'" % str1)):
           
           print c.fetchall()
           
          
       if (c.execute("SELECT * FROM info WHERE LastName like '%s'" % str2)):
           
           print c.fetchall()
           
       if (c.execute("SELECT * FROM info WHERE EmailId like '%s'" % str3)):
           
           print c.fetchall()
           
        """       
       #save changes
       conn.commit()
           
           
            
       #close database
       conn.close()
           
       
       
#creating object             
obj = Read()
#Insert the path of the file
f = raw_input('Enter path of the csv file :')
#calling method
my_List = obj.csv_reader(f)
obj.insert(my_List)
"""
#creating a list
obj.a = []
obj.Firstname=raw_input('Enter the first name \n')
obj.Lastname=raw_input('Enter the Last name \n')
obj.EmailId=raw_input('Enter the Email Id \n')
(obj.a).append(obj.Firstname)
(obj.a).append(obj.Lastname)
(obj.a).append(obj.EmailId)
obj.insert(my_List,obj.a)  
"""
