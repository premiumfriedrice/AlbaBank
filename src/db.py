import mysql.connector
from typing import Tuple
from datetime import datetime
import yaml
with open("env.yaml", "r") as f:
    config = yaml.safe_load(f)

dbconn = mysql.connector.connect(host=config["HOST"], user=config["USERNAME"], password=config["PASSWORD"], database=config["DB_NAME"])

cur=dbconn.cursor()

def createUserTable():
    usersqlf = "CREATE TABLE users (id INTEGER PRIMARY KEY AUTO_INCREMENT , username VARCHAR(45) UNIQUE, password VARCHAR(45), birthdate DATETIME, email VARCHAR(45) UNIQUE, checking DECIMAL(10), savings DECIMAL(10))"
    cur.execute(usersqlf)
    dbconn.commit()
    
def seedUserTable():
    addUser(0, "Billgates2", "microSawft", "1965-09-22", "billgates@microsoft.com", 10000, 2000000)
    addUser(0, "JeffyBezzos", "amaZ4n", "1970-04-22", "bigJeff@amazon.com", 3820184873, 383726418)
    addUser(0, "Bamaboy21", "rollt1de", "1982-01-02", "bleedcrimson@bama.com", 1284736281, 9483628374)
    addUser(0, "YEEZUS", "donda", "1985-04-01", "ihate@adidas.com", 1288333333, 1383291737)
    
def addUser(id, username, password, birthdate, email, checking, savings):
    cur.execute("INSERT INTO users (id, username, password, birthdate, email, checking, savings) VALUES(%s, %s, %s, %s, %s, %s, %s)", (id, username, password, birthdate, email, checking, savings))
    dbconn.commit()


def validateUser():
    pass


def getChecking(id):
    sql = f"SELECT checking FROM users WHERE id = {id}"
    cur.execute(sql)
    checking = float(cur.fetchone()[0])
    print(checking)
    return checking 
    

def getSavings(id):
    sql = f"SELECT savings FROM users WHERE id = {id}"
    cur.execute(sql)
    checking = float(cur.fetchone()[0])
    print(checking)
    return checking 

def alterChecking():
    pass

def alterSacvings():
    pass