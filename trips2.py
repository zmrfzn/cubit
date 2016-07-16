from mysql import connector
import mysql.connector.errors
from urllib2 import urlopen
import json

trip_ids=[]
#db connection object
conn = connector.connect(host='localhost',user='root',passwd='root',db='cubito')
cursor = conn.cursor()


def getDetail(trip_id,current_state):
	while (current_state=="RUNNING"):
		trip_detail = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id))
		print trip_detail["status"]+":"+trip_detail["trip_id"]
		#Fail Safe
		if trip_detail["status"] == "COMPLETED":
			current_state="COMPLETED"
			break
		
	return

#get trip ids
def getTripData():
	flag=1
	for id in range(2):
		trip_id = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php"))
		current_state = "RUNNING"
		print str(trip_id["trip_id"])+"START"
		dummy = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id["trip_id"]))
		current_state = dummy["status"]
		getDetail(trip_id["trip_id"],current_state)
		print str(trip_id["trip_id"])+"STOP"
		

getTripData()
