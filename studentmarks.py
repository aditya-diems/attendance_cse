import pandas as pd
import mysql.connector
import pickle
import csv


def getmarks(examtype, year, div, roll):
    marks = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='marks_cse')
    markCur = marks.cursor()
    tablename = examtype+'-'+year+'-'+div
    try:
        sql = "SELECT * FROM `{}` WHERE `ROLL`='{}'".format(tablename, roll)
        markCur.execute(sql)
        data = markCur.fetchall()
        sql = "SHOW COLUMNS FROM `{}`".format(tablename)
        markCur.execute(sql)
        cols = markCur.fetchall()
        column = []
        for i in cols:
            column.append(i[0])
    except Exception as e:
        column = []
        data = [()]
        print(e)

    marks.close()
    return [data[0], column]


def allowgrievances(roll, examtype, year, division, subject, newmarks):
    marks = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='marks_cse')
    markCur = marks.cursor()

    tablename = examtype+'-'+year+'-'+division

    # print(roll, examtype, year, division, subject, newmarks)
    sql = "UPDATE `{}` SET `{}`='{}' WHERE `roll`='{}'".format(
        tablename, subject, newmarks, roll)
    markCur.execute(sql)
    marks.commit()

    sql = "UPDATE `grievance` SET `Status`='Accepted' WHERE `Roll`='{}' AND `Subject`='{}' ".format(
        roll, subject)
    markCur.execute(sql)
    marks.commit()

    marks.close()


def rejectgrievances(roll, examtype, year, division, subject, marks):
    marks = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='marks_cse')
    markCur = marks.cursor()

    sql = "UPDATE `grievance` SET `Status`='Rejected' WHERE `Roll`='{}' AND `Subject`='{}'".format(
        roll, subject)
    markCur.execute(sql)
    marks.commit()

    marks.close()
