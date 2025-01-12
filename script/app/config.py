import os
import osmnx as ox
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
startTime = datetime.now()

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "NY-NAV-BABY"

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    """
    bike_dangerous = os.path.join(basedir,"CSV/bike_dangerous.graphml")
    bike_safest = os.path.join(basedir,"CSV/bike_safest.graphml")
    bike_safest_ratio = os.path.join(basedir,"CSV/bike_safest_ratio.graphml")
    drive_dangerous = os.path.join(basedir,"CSV/drive_dangerous.graphml")
    drive_safest = os.path.join(basedir,"CSV/drive_safest.graphml")
    drive_safest_ratio = os.path.join(basedir,"CSV/drive_safest_ratio.graphml")
    walk_dangerous = os.path.join(basedir,"CSV/walk_dangerous.graphml")
    walk_safest = os.path.join(basedir,"CSV/walk_safest.graphml")
    walk_safest_ratio = os.path.join(basedir,"CSV/walk_safest_ratio.graphml")
    """

    G_drive_safest = ox.io.load_graphml(filepath="script/app/CSV/drive_safest.graphml")   
    G_walk_safest = ox.io.load_graphml(filepath="script/app/CSV/walk_safest.graphml")   
    G_bike_safest = ox.io.load_graphml(filepath="script/app/CSV/bike_safest.graphml")   
    G_drive_dangerous = ox.io.load_graphml(filepath="script/app/CSV/drive_dangerous.graphml")   
    G_walk_dangerous = ox.io.load_graphml(filepath="script/app/CSV/walk_dangerous.graphml")   
    G_bike_dangerous = ox.io.load_graphml(filepath="script/app/CSV/bike_dangerous.graphml")   
    G_drive_safest_ratio = ox.io.load_graphml(filepath="script/app/CSV/drive_safest_ratio.graphml")   
    G_walk_safest_ratio = ox.io.load_graphml(filepath="script/app/CSV/walk_safest_ratio.graphml") 
    G_bike_safest_ratio = ox.io.load_graphml(filepath="script/app/CSV/bike_safest_ratio.graphml")   
    


if __name__ == "__main__":
    print(basedir)
    print(Config.bike_dangerous)