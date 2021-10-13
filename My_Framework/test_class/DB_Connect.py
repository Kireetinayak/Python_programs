import mysql.connector
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('10.184.20.34', '1521', service_name='ORQ688A.int.thomsonreuters.com')
mydb = cx_Oracle.connect(user="ICDMASTER", password="icdmaster", dsn=dsn_tns)
db=mydb.cursor()