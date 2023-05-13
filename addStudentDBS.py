import pandas as pd
from routes import mysql_stud
import mysql.connector
import pickle

fs = 'subinfo.pkl'


def addInSubject(roll, name, year, div):
    at_btech = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_btech')
    at_ty = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_ty')
    at_sy = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='theory_sy')

    btech = at_btech.cursor()
    ty = at_ty.cursor()
    sy = at_sy.cursor()

    fsub = open(fs, 'rb')
    subs_btech = pickle.load(fsub)
    # print(year)

    if year == "BTECH":
        for i in subs_btech['Theory'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division) VALUES (%s,%s,%s)"
            values = (str(roll), name, div)
            btech.execute(sql, values)
            at_btech.commit()

    elif year == 'TY':
        for i in subs_btech['Theory'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division) VALUES (%s,%s,%s)"
            values = (str(roll), name, div)
            ty.execute(sql, values)
            at_ty.commit()

    elif year == 'SY':
        for i in subs_btech['Theory'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division) VALUES (%s,%s,%s)"
            values = (str(roll), name, div)
            sy.execute(sql, values)
            at_sy.commit()
    at_btech.close()
    at_ty.close()
    at_sy.close()


def addInPractical(roll, name, year, div, batch):
    ap_btech = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_btech')
    ap_ty = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_ty')
    ap_sy = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='practical_sy')

    btechP = ap_btech.cursor()
    tyP = ap_ty.cursor()
    syP = ap_sy.cursor()

    fsub = open(fs, 'rb')
    subs_btech = pickle.load(fsub)

    if year == "BTECH":
        for i in subs_btech['Practical'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division,batch) VALUES (%s,%s,%s,%s)"
            values = (str(roll), name, div, batch)
            btechP.execute(sql, values)
            ap_btech.commit()

    elif year == 'TY':
        for i in subs_btech['Practical'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division,batch) VALUES (%s,%s,%s,%s)"
            values = (str(roll), name, div, batch)
            tyP.execute(sql, values)
            ap_ty.commit()

    elif year == 'SY':
        for i in subs_btech['Practical'][year]:
            sql = "INSERT INTO "+"`"+i+"`" + \
                " (roll,name,division,batch) VALUES (%s,%s,%s,%s)"
            values = (str(roll), name, div, batch)
            syP.execute(sql, values)
            ap_sy.commit()

    ap_btech.close()
    ap_ty.close()
    ap_sy.close()


def addLoginInfo(roll, name, year):
    print('in ad in login')
    logindbs = mysql.connector.connect(
        user='root', password='mousehead@2931', host='localhost', database='logincse')
    lo_cur = logindbs.cursor()
    authoritiy = 'student'
    username = name.split()[0]
    password = str(roll)
    email = year+'@gmail.com'
    print(type(authoritiy), type(username), type(password), type(email))
    lo_cur.execute('INSERT INTO account VALUES (%s, %s, %s, %s, %s)',
                   (roll, authoritiy, username, password, email))
    logindbs.commit()
    logindbs.close()


def addstud(roll, name, year, division, batch):
    try:
        cur = mysql_stud.connection.cursor()
        sql = "INSERT INTO " + year + \
            " (ROLL_NO, NAME, YEAR, DIVISION, BATCH) VALUES (%s, %s, %s, %s, %s)"
        value = (roll, name, year, division, batch)
        cur.execute(sql, value)
        mysql_stud.connection.commit()
        addInSubject(roll, name, year, division)
        addInPractical(roll, name, year, division, batch)
        addLoginInfo(roll, name, year)
    except:
        print('PRN already exist')
