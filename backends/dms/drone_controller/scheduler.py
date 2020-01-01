import pyodbc
import time
from os import system as sys
from math import sqrt

connection_SQL = pyodbc.connect() ####### Won't put it here. I'll add these credentials during deployment.
cursor_SQL = connection_SQL.cursor()

class DroneStock():
    
    def __init__(self,latitude,longitude,mission_type,priority,expected_mission_duration,num_drones=1):
        self.lat = latitude
        self.long = longitude
        self.mission_type = mission_type
        self.priority = priority
        self.expected_mission_duration = expected_mission_duration
        self.num_drones = num_drones
        self.nearest_drones = []

    def location_dist(loc1,loc2):
        return sqrt((loc1[0]-loc2[0])**2 + (loc1[0]-loc2[0])**2)
    
    def search_nearest(self):
        cursor_SQL.execute(f"SELECT TOP {self.num_drones} drones WHERE mission_status == '111111' AND {self.priority} > mission_criticality AND location.STX BETWEEN {self.long+0.0005} AND {self.long - 0.0005} AND location.STY BETWEEN {self.lat + 0.0005} AND {self.lat - 0.0005} ORDER BY (POW(location.STX-{self.long},2) + POW(location.STY-{self.lat},2);")
        row = cursor_SQL.fetchone()
        while row:
            if self.checkSuitable(row):
                self.nearest_drones.append(row)
            row.fetchone()
        return self.nearest_drones

    def findSuitable(self):
        if self.num_drones is not 1:
            self.nearest_drones.sort(key=lambda x: location_distance(drone[2],(self.lat,self.long))  ### Not sure if long comes first in DB
            return self.nearest_drones[:self.num_drones]
        return self.nearest_drones
