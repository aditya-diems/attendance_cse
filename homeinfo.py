import pandas as pd
from routes import mysql_stud
import mysql.connector


def getleccount(subs):
    at_btech = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_btech')
    at_ty = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_ty')
    at_sy = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_sy')
    ap_btech = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_btech')
    ap_ty = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_ty')
    ap_sy = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_sy')

    btech = at_btech.cursor()
    ty = at_ty.cursor()
    sy = at_sy.cursor()

    btechP = ap_btech.cursor()
    tyP = ap_ty.cursor()
    syP = ap_sy.cursor()

    count = {}
    for i in subs:
        for j in subs[i]:
            for k in subs[i][j]:
                for l in subs[i][j][k]:
                    if i == 'BTECH':
                        if k == 'THEORY':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            btech.execute(sql)
                            cols = btech.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[3:]
                            tempcount = 0
                            for fig in cols:
                                sql = "SELECT `{}` from `{}` WHERE `division`='{}'".format(
                                    fig, l, j)
                                btech.execute(sql)
                                data = btech.fetchall()
                                for zz in range(len(data)):
                                    data[zz] = data[zz][0]
                                if any(tenz > 0 for tenz in data):
                                    tempcount += max(data)
                            if 'other attendance' not in l:
                                if j in count:
                                    count[j][l] = tempcount
                                else:
                                    count[j] = {}
                                    count[j][l] = tempcount

                        elif k == 'PRACTICAL':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            btechP.execute(sql)
                            cols = btechP.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[4:]
                            tp = []
                            for m in subs[i][j][k][l]:
                                tempcount = 0
                                for fig in cols:
                                    sql = "SELECT `{}` from `{}` WHERE `batch`='{}'".format(
                                        fig, l, m)
                                    btechP.execute(sql)
                                    data = btechP.fetchall()
                                    for zz in range(len(data)):
                                        data[zz] = data[zz][0]
                                    if any(tenz > 0 for tenz in data):
                                        tempcount += max(data)
                                tp.append(tempcount)

                            if j in count:
                                count[j][l] = tp
                            else:
                                count[j] = {}
                                count[j][l] = tp

                    elif i == 'TY':
                        if k == 'THEORY':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            ty.execute(sql)
                            cols = ty.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[3:]
                            tempcount = 0
                            for fig in cols:
                                sql = "SELECT `{}` from `{}` WHERE `division`='{}'".format(
                                    fig, l, j)
                                ty.execute(sql)
                                data = ty.fetchall()
                                for zz in range(len(data)):
                                    data[zz] = data[zz][0]
                                if any(tenz > 0 for tenz in data):
                                    tempcount += max(data)
                            if 'other attendance' not in l:
                                if j in count:
                                    count[j][l] = tempcount
                                else:
                                    count[j] = {}
                                    count[j][l] = tempcount

                        elif k == 'PRACTICAL':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            tyP.execute(sql)
                            cols = tyP.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[4:]
                            tp = []
                            for m in subs[i][j][k][l]:
                                tempcount = 0
                                for fig in cols:
                                    sql = "SELECT `{}` from `{}` WHERE `batch`='{}'".format(
                                        fig, l, m)
                                    tyP.execute(sql)
                                    data = tyP.fetchall()
                                    for zz in range(len(data)):
                                        data[zz] = data[zz][0]
                                    if any(tenz > 0 for tenz in data):
                                        tempcount += max(data)
                                tp.append(tempcount)

                            if j in count:
                                count[j][l] = tp
                            else:
                                count[j] = {}
                                count[j][l] = tp

                    elif i == 'SY':
                        if k == 'THEORY':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            sy.execute(sql)
                            cols = sy.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[3:]
                            tempcount = 0
                            for fig in cols:
                                sql = "SELECT `{}` from `{}` WHERE `division`='{}'".format(
                                    fig, l, j)
                                sy.execute(sql)
                                data = sy.fetchall()
                                for zz in range(len(data)):
                                    data[zz] = data[zz][0]
                                if any(tenz > 0 for tenz in data):
                                    tempcount += max(data)
                            if 'other attendance' not in l:
                                if j in count:
                                    count[j][l] = tempcount
                                else:
                                    count[j] = {}
                                    count[j][l] = tempcount

                        elif k == 'PRACTICAL':
                            sql = "SHOW COLUMNS FROM `{}`".format(l)
                            syP.execute(sql)
                            cols = syP.fetchall()
                            for tit in range(len(cols)):
                                cols[tit] = cols[tit][0]
                            cols = cols[4:]
                            tp = []
                            for m in subs[i][j][k][l]:
                                tempcount = 0
                                for fig in cols:
                                    sql = "SELECT `{}` from `{}` WHERE `batch`='{}'".format(
                                        fig, l, m)
                                    syP.execute(sql)
                                    data = syP.fetchall()
                                    for zz in range(len(data)):
                                        data[zz] = data[zz][0]
                                    if any(tenz > 0 for tenz in data):
                                        tempcount += max(data)
                                tp.append(tempcount)

                            if j in count:
                                count[j][l] = tp
                            else:
                                count[j] = {}
                                count[j][l] = tp

    at_btech.close()
    at_sy.close()
    at_ty.close()
    ap_btech.close()
    ap_sy.close()
    ap_ty.close()
    return count
