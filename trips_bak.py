from mysql import connector
import mysql.connector.errors
from urllib2 import urlopen
import json

trip_ids=[]
trip_details={}
#db connection object
conn = connector.connect(host='localhost',user='root',passwd='root',db='cubito')
cursor = conn.cursor()

#get trip ids
def getTripId():
    for id in range(0,2):
        trip_ids.append(json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php")))

    for trip_id in trip_ids:
        cursor.execute("insert into trips (trip_id) values('"+trip_id["trip_id"]+"')")
        conn.commit()
        #print trip_id["trip_id"]



def getTripData():

    cursor.execute("select trip_id from trips limit 2")
    #ids= cursor.fetchall()
    ids = trip_ids
    #print ids
    for trip_id in ids:
        print trip_id
        key=1
        trip_detail = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id["trip_id"]))
        while(trip_detail["trip_id"]==trip_id["trip_id"] and trip_detail["status"]=="RUNNING"):
            trip_detail = json.load(urlopen("http://cubito.co.in/assignment/gpslocation.php?trip_id="+trip_id["trip_id"]))
            print str(trip_detail["status"])+str(key)
            #trip_details[trip_detail["lastupdate"]] = 
            #print trip_detail["location"]
            
            if(trip_detail["status"]=="COMPLETED"):
                trip_detail["status"]="COMPLETED"
                print str(key)+"completed"
                key=key+1





getTripId()
getTripData()