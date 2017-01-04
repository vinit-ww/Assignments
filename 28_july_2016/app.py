#app.py
import falcon
import json
from db_client import *

class NoteResource(object):
    
    def on_get(self,req,resp):
	   	#handle get request
		conn=psycopg2.connect(database="test1",user="postgres",password="test",host="127.0.0.1",port="5432")
		c=conn.cursor()
		c.execute("select * from Books ")
		rows=c.fetchall()
		result={'note': rows}
		resp.body=json.dumps(result)
		c.close()
        
api = falcon.API()
api.add_route('/notes', NoteResource())
