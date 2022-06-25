import mysql.connector
import pandas as pd
import ftplib
import os
import telegram_send
from datetime import datetime, timedelta

last_date  = datetime.today() - timedelta(days=1)
this_year  = last_date.strftime("%Y")
this_month = last_date.strftime("%m")

try:
    month = months
    year = years
except:
    month = this_month
    year = this_year
    
if month == "01":
    month1 = "Januari"
if month == "02":
    month1 = "Februari"
if month == "03":
    month1 = "Maret"
if month == "04":
    month1 = "April"
if month == "05":
    month1 = "Mei"
if month == "06":
    month1 = "Juni"
if month == "07":
    month1 = "Juli"
if month == "08":
    month1 = "Agustus"
if month == "09":
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

try:
    update.message.reply_text('Dataplan '+month1+' '+year+' updated by '+user['first_name'])
except:
    os.environ["https_proxy"] = "https://10.59.66.1:8080"
    telegram_send.send(messages=['Autoupdate dataplan '+month1+' '+year+' successfully'])