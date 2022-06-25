import mysql.connector
import pandas as pd
import ftplib
import os
    
if month == "1":
    month1 = "Januari"
if month == "2":
    month1 = "Februari"
if month == "3":
    month1 = "Maret"
if month == "4":
    month1 = "April"
if month == "5":
    month1 = "Mei"
if month == "6":
    month1 = "Juni"
if month == "7":
    month1 = "Juli"
if month == "8":
    month1 = "Agustus"
if month == "9":
    month1 = "September"
if month == "10":
    month1 = "Oktober"
if month == "11":
    month1 = "November"
if month == "12":
    month1 = "Desember"

# DB CONFIG
conn = mysql.connector.connect(
    host="10.47.150.170",
    user="erikgin",
    password="V4Cged64",
    database="jabar_performance"
)
# QUERY
query = '''SELECT * FROM jabar_data_plan_'''+year+''' WHERE month = "''' + \
    month+'''" AND YEAR = "'''+year+'''";'''

name_file = 'DATA_JABAR_'+month1+'_'+year+'.csv'
df = pd.read_sql(query, conn)

df.to_csv(
    '''F:/KY/dataplan/'''+name_file, index=False)

session = ftplib.FTP('10.3.107.222', 'sqajabar', 'Jabar2018')
file = open('F:/KY/dataplan/DATA_JABAR_' +
            month1+'_'+year+'.csv', 'rb')
session.storbinary(
    'STOR /DATA_SQA/DATA_STATISTIK_SQA/DATA JABAR/DATA_JABAR_'+month1+'_'+year+'.csv', file)
file.close()
session.quit()