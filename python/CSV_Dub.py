import csv
import sqlite3
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

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
       
       my_list = [] 
       #Create table
      # c.execute('''CREATE TABLE info( FirstName text ,LastName text ,EmailId text )''')
      
     #  for t in my_List :
     #      c.execute("insert into info(FirstName , LastName ,EmailId) values (?,?,?)",(t[0],t[1],t[2],)) 
         
       
       if (c.execute("SELECT * FROM info ")):
           r =c.fetchall()
           for member in r:
               my_list.append(member)
              
        
      
          
       #save changes
       conn.commit()
           
       #close database
       conn.close()
       
       return my_list    

   def table(self,data):
       doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)   
       # container for the 'Flowable' objects
       elements = []
       t=Table(data)
       t.setStyle(TableStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black),('BOX',(0,0),(-1,-1),0.50,colors.red)]))
       elements.append(t)
       #write the document to list
       doc.build(elements)
        
#creating object             
obj = Read()
#Insert the path of the file
f=raw_input('Enter path of the csv file :')
#calling method
my_List = obj.csv_reader(f)
_list=obj.insert(my_List)
obj.table(my_List)
