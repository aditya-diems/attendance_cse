import pandas as pd
from routes import mysql_stud
import mysql.connector
import pickle
import csv


def addmarks(file_path, exam, year, div):
    marks = mysql.connector.connect(
        user='root', password='', host='localhost', database='marks_cse')
    markCur = marks.cursor()
    fobj = open(file_path, 'r')
    data = csv.reader(fobj)
    for i in data:
        cols = i
        break
    columns = ''
    for i in cols:
        if i == cols[-1]:
            columns += '`{}` TEXT NOT NULL'.format(i)
        else:
            columns += '`{}` TEXT NOT NULL,'.format(i)
    tablename = exam+'-'+year+'-'+div
    try:
        sql = 'CREATE TABLE `'+tablename+'` ('+columns+')'
        markCur.execute(sql)
        marks.commit()
    except Exception as e:
        print(e)
    for i in data:
        if i == cols:
            continue
        row = ''
        for j in range(len(i)):
            if j == len(i)-1:
                row += "'{}'".format(i[j])
            else:
                row += "'{}',".format(i[j])
        sql = 'INSERT INTO `'+tablename+'` VALUES (' + row + ')'
        markCur.execute(sql)
        marks.commit()

    marks.close()
