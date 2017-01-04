#parsing information from a url with the help of urllib3 and Beautiful Soup and storing in a database
import sqlite3
import urllib3
from bs4 import BeautifulSoup
class Parser:
    a=[]
    def get(self,url):
        http=urllib3.PoolManager()
        r = http.request('GET',url)
        return r.data,r.status
        
    def beautiful(self,html_doc):
        soup=BeautifulSoup(html_doc,"html.parser")
        attr=soup.find("div",class_="field-item even")
        attr=soup.find("div",class_="field-item even")
        row=attr.find_all("a")
        for i in row:
            self.a.append(i.get_text())
        return self.a
        '''
        First_Notice=attr.find("a")
        Second_Notice=First_Notice.find_next_sibling("a")
        self.a.append(soup.title.string)
        Third_Notice=Second_Notice.find_next_sibling("a")
        self.a.append(First_Notice.string)
        self.a.append(Second_Notice.string)
        return self.a
        '''
        
    def insert(self,my_List):
        
        #connecting database 
        conn=sqlite3.connect('myDatabase')
       
        #once we have the connection we can create the cursor object to execute() query
        c = conn.cursor()
       
        #Create table
      #  c.execute('''CREATE TABLE sum(Title text unique ,Notice1 text unique,Notice2 text unique)''')
      
      #  c.execute("insert into sum(Title ,Notice1 ,Notice2) values (?,?,?)",(my_List[0],my_List[1],my_List[2],))
            
            
        if (c.execute("SELECT * FROM sum ")):
            r =c.fetchall()
            for member in r:
               print '\n'.join(member)
               
        
        
        #save changes
        conn.commit()
        #close database
        conn.close()


            
        
obj=Parser()
r=raw_input('Enter the url=\n') 
html_doc,status=obj.get(r)
if status == 200:
    _list=obj.beautiful(html_doc)
    obj.insert(_list)
else:
    print "OOPS! Error please Try again latter"
