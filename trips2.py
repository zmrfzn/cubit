from mysql import connector
import mysql.connector.errors
from urllib2 import urlopen
import json

trip_ids=[]
#db connection object
conn = connector.connect(host='localhost',user='root',passwd='root',db='cubito')
cursor = conn.cursor()

#get trip ids
def getTripData():
	count=0
	flag=1
	for id in range(2):
		trip_ids.append(json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php")))
	for trip_id in trip_ids:
		print flag
		print str(count)+":"+str(trip_id["trip_id"])
		while (True):
			trip_detail = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id["trip_id"]))
			print trip_detail["status"]+":"+trip_detail["trip_id"]
   			count=count+1     	
        	if(count==5):
        		print "break"
        		break
        		flag=flag+1
		#print trip_id["trip_id"]


getTripData()

