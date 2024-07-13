import sqlite3 as sql3 
from datamodel import *

class Database:
    def __init__(self,name:str, newDB:bool=False) -> None:
        self.connection = sql3.connect(name)
        if newDB:
            self.newDB()

    def newDB(self,filename:str=''):
        '''Create the tables inside the database'''
        pass

