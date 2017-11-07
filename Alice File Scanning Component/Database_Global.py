import os
import sqlite3 as mysql
def is_array(var):
    return isinstance(var, (list, tuple))

def SQL_Prep(Var): #Will turn lists/Tuples into strings e.g. (Hello, World)
    if not is_array(Var):
        return Var
    String = ''.join(['(', Var[0]]) 
    for i in range(1, len(Var)):
        String = ''.join([String, ', ', Var[i]])
    String = ''.join([String, ')'])
    return String

def Check_Database(path, Create=False): 
    if (os.path.exists(path) == False) and (Create == False):
        return False

    else:
        return mysql.connect(path)
