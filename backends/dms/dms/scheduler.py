import pyodbc
import time
from os import system as sys

connection_SQL = pyodbc.connect() ####### Won't put it here. I'll add these credentials during deployment.
cursor_SQL = connection_SQL.cursor()

class DroneStock():
    
    def __init__(self,lat,long,mission_type,priority,expected_mission_duration):
        self.lat = lat
        self.nearest_drones = []
        self.availablity = {}
      # complete this part
    
    def search_nearest():
       #Rename the drones in the query, I don't remember the names of the attributes in the table
        cursor_SQL.execute(f"SELECT TOP 6 drones WHERE lon BETWEEN {self.location[1]+0.0005} AND {self.location[1] - 0.0005} AND lat BETWEEN {self.location[0] + 0.0005} AND {self.location[0] - 0.0005} ORDER BY (POW(lon-{self.location[1]},2) + POW(lon-{self.location[0]},2) " )
        row = cursor_SQL.fetchone()
        while row:
            self.nearest_drone.append(row)
            row.fetchone()
        return self.nearest_drones
    
    #This is the main logic. Check the other conditions like availability, priority, mission_status, etc before assigning a drone to the given mission.
    #I'm sleeping now. GN.
