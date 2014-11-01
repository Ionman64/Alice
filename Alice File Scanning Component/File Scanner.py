import os
import time
from Database_Global import *

def create_tables(Conn):
    SQL = ('CREATE TABLE "File_Info" ("ID" TEXT PRIMARY KEY  NOT NULL  DEFAULT (null) ,"Create_Time" DATETIME,"Create_Date" DATETIME,"Modify_Time" DATETIME,"Modify_Date" DATETIME)')
    Conn.execute(SQL)
    SQL = ('CREATE TABLE "Files" ("ID" TEXT PRIMARY KEY  NOT NULL , "Filename" TEXT, "Path" TEXT, "File_Ext" TEXT, "Size" INTEGER)')
    Conn.execute(SQL)
    
def file_time_parse(File_Data, Creation=True): #File_Data should be the os.stat data on the file, Creation dictates wether it is the creation time or the modify time
    if (Creation == True):
        File_Stamp = time.strftime("%Y/%m/%d|%H:%M:%S", time.gmtime(File_Data.st_ctime))
    else:
        File_Stamp = time.strftime("%Y/%m/%d|%H:%M:%S", time.gmtime(File_Data.st_mtime))
    File_Date = File_Stamp.split("|")[0]
    File_Time = File_Stamp.split("|")[1]
    return (File_Date, File_Time)

def filemap(path):
    i = 0;
    Start_Dir = path
    dir_files = []
    for (path, dirs, files) in os.walk(path):
        for l in files:
            filepath = (path + "\\" + l)
            if (os.path.exists(filepath) == False):
                with open(Start_Dir + "\\File_Scanning Log.txt", "a") as file:
                    file.write("Error - " + filepath + "\n")
                break
            filestat = os.stat(filepath)
            CFile_Date, CFile_Time = file_time_parse(filestat)
            MFile_Date, MFile_Time = file_time_parse(filestat, False)
            file_info = {'Filename' : os.path.splitext(l)[0], 'Path' : path, 'Ext' : os.path.splitext(l)[1], 'Size' : filestat.st_size, 'Create_Time' : CFile_Time, 'Create_Date' : CFile_Date, 'Modify_Time' : MFile_Time, 'Modify_Date' : MFile_Date}
            dir_files.append(file_info)
    return dir_files

def zerofill(i):
    length = len(str(i))
    zeros = ('0' * (13-length))
    return zeros + str(i)

def main(path):
    DB = Check_Database(path + "\\" + Ext('Filemap'), True)
    Conn = DB.cursor()
    Conn.execute('SELECT * FROM sqlite_master WHERE type="table"')
    Result = Conn.fetchall()
    if (Result):
        Conn.execute('DELETE FROM File_Info')
        Conn.execute('DELETE FROM Files') #Delete the Contents of the Tables
    else:
        create_tables(Conn)
    Conn.close()
    DB.commit()
    Conn = DB.cursor()
    index = 0
    for Entry in filemap(path):
        index+=1
        ID = zerofill(index)
        SQL1 = ('INSERT INTO Files VALUES ("%s", "%s", "%s", "%s", %s)' % (ID, Entry['Filename'], Entry['Path'], Entry['Ext'], Entry['Size']))
        SQL2 = ('INSERT INTO File_info VALUES ("%s", "%s", "%s", "%s", "%s")' % (ID, Entry['Create_Time'], Entry['Create_Date'], Entry['Modify_Time'], Entry['Modify_Date']))
        Conn.execute(SQL1)
        Conn.execute(SQL2)
    DB.commit()
    Conn.close()
    return True

main("F:\\Mp4 Files")
