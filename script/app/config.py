import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "NY-NAV-BABY"
    bike_dangerous = os.path.join(basedir,"CSV\\bike_dangerous.graphml")
    bike_safest = os.path.join(basedir,"CSV\\bike_safest.graphml")
    bike_safest_ratio = os.path.join(basedir,"CSV\\bike_safest_ratio.graphml")
    drive_dangerous = os.path.join(basedir,"CSV\\drive_dangerous.graphml")
    drive_safest = os.path.join(basedir,"CSV\\drive_safest.graphml")
    drive_safest_ratio = os.path.join(basedir,"CSV\\drive_safest_ratio.graphml")
    walk_dangerous = os.path.join(basedir,"CSV\\walk_dangerous.graphml")
    walk_safest = os.path.join(basedir,"CSV\\walk_safest.graphml")
    walk_safest_ratio = os.path.join(basedir,"CSV\\walk_safest_ratio.graphml")

if __name__ == "__main__":
    print(basedir)
    print(Config.bike_dangerous)