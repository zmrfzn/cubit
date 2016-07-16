from mysql import connector
import mysql.connector.errors as CE
from urllib2 import urlopen
from multiprocessing import pool
import json

#db connection object
conn = connector.connect(host='localhost',user='root',passwd='root',db='cubito')
cursor = conn.cursor()


def getDetail(trip_id,current_state):
	
	location = []
	while (current_state=="RUNNING"):
		trip_detail = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id))
		print trip_detail["status"]+":"+trip_detail["trip_id"]
		
		location.append(str(trip_detail["location"]["latitude"])+","+str(trip_detail["location"]["longitude"]))
		
		#Fail Safe
		if trip_detail["status"] == "COMPLETED":
			current_state="COMPLETED"
			json_loc= json.dumps(location)
			break
		
	return json_loc
#get trip ids
def getTripData():
	flag=1
	for id in range(2):
		trip_id = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php"))
		current_state = "RUNNING"
		print str(trip_id["trip_id"])+"START"
		dummy = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id["trip_id"]))
		current_state = dummy["status"]
		location = getDetail(trip_id["trip_id"],current_state)
		print location
		try:
			cursor.execute("insert into trips values('"+trip_id["trip_id"]+"','"+location+"')")
			conn.commit()
		except (CE.Error ,Exception) as e:
			print e
		
		print str(trip_id["trip_id"])+"STOP"


getTripData()
