#app.py
import falcon
import json
import psycopg2

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

    def on_post(self,req,resp):
		#Handle post requests
		result=req.stream.read()
		print result



api = falcon.API()
api.add_route('/notes',NoteResource())
