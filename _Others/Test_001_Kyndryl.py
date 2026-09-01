#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import pyodbc # pip install pyodbc
import psycopg2 # pip install psycopg2
from datetime import date
import config # file config.py
# import db2_select # file db2_select.py
# import postgresql_delete # file postgresql_delete.py
# import postgresql_insert # file postgresql_insert.py
# import sql_insert # file sql_insert.py
print("Author: ", config.author)
#-------------------------------------------------------------------------------
# Cria o Connection e o Cursor com o DB2 via ODBC
#-------------------------------------------------------------------------------
print("DB2 Connection: ", config.db2["connection"])
#con = pyodbc.connect(config.db2["connection"])
#cur = con.cursor()
#-------------------------------------------------------------------------------
# Table e SQL usados para o Select e Insert com replace para a Data desejada
#-------------------------------------------------------------------------------
sql_date = str(date.today())
sql_table = "CICS_ABENDS_T"
sql_select =  """
------------------------------------------------------------
-- CICS_ABENDS_T;
------------------------------------------------------------
SELECT DATE(START_TIMESTAMP) AS DATE
     , TIME(START_TIMESTAMP) AS TIME
     , MVS_SYSTEM_ID
     , CICS_SYSTEM_ID
     , TRANSACTION_ID
     , TRANSACTION_TYPE
     , CASE WHEN PROGRAM_NAME = '' THEN 'NONE'
           ELSE PROGRAM_NAME
           END AS PROGRAM_NAME
     , ABEND_CODE_ORIGIN
     , ABEND_CODE_CURRENT
     , CPU_SEC
  FROM DRLFIS.CICS_ABENDS_T
 WHERE MVS_SYSTEM_ID IN ('FIDY', 'FPR1')
   AND START_TIMESTAMP >= TIMESTAMP(DATE('$#@DATE@#$') - 1 DAY, '00.00.00')
  WITH UR;
------------------------------------------------------------
"""
sql_select = sql_select.replace("$#@DATE@#$", sql_date)
print("SQL Select: ", sql_select)
#-------------------------------------------------------------------------------
# Executa o Select no DB2 e armazena os campos e os valores em formato Array
#-------------------------------------------------------------------------------
#try:
#    cur_status = cur.execute(sql_select)
#    cur_desc = cur.description
#    cur_rall = cur.fetchall()
cur_desc = [["KEY"], ["DESCRPTION"]]
cur_rall = [[1, "TEST 01"], [2, "TEST 02"]]
#-------------------------------------------------------------------------------
# Em caso de erro apresenta o comando SQL e mensagem de erro do DB2
#-------------------------------------------------------------------------------
#except (Exception, pyodbc.DatabaseError) as error:
#    print("SQL Error, DB2:")
#    print("SQL Select:", sql_select)
#    print("SQL Error:", error)
#-------------------------------------------------------------------------------
# Fecha o Cursor e o Connection com o DB2
#-------------------------------------------------------------------------------
#cur.close()
#con.close()
#-------------------------------------------------------------------------------
# Cria o Prefix do SQL com o comando Insert e o nome dos campos sem os valores  
#-------------------------------------------------------------------------------
sql_prefix = "INSERT INTO " + sql_table + " ("
sql_sufix = ") VALUES ("
sql_desc = ""
cur_len = len(cur_rall)
col_last = len(cur_desc) - 1 
#-------------------------------------------------------------------------------
for col_index, col_desc in enumerate(cur_desc):
    if col_index == col_last:
        sql_desc += col_desc[0]
    else:
        sql_desc += col_desc[0] + ", "    
#-------------------------------------------------------------------------------
# Com os valores retornados do SELECT monta os comandos Insert
# e armazena os comandos Insert agora com os valores em formato Array
#-------------------------------------------------------------------------------
sql_list = list(range(cur_len))
#-------------------------------------------------------------------------------
for row_index, row_values in enumerate(cur_rall):
    sql_values = ""
    str_asp = ""
    for col_index, col_value in enumerate(row_values):
        str_value = str(col_value).strip()
        if str_value.isnumeric() == True:
            str_asp = ""
        else:
            str_asp = "'"
        if col_index == col_last:
            sql_values += str_asp + str_value + str_asp
        else:
            sql_values += str_asp + str_value + str_asp + ", "
    sql_insert = sql_prefix + sql_desc + sql_sufix + sql_values + ");"
    sql_list[row_index] = sql_insert
#-------------------------------------------------------------------------------
# Cria o Connection e o Cursor com o PostGreSQL
#-------------------------------------------------------------------------------
# con = psycopg2.connect(config.postgresql[connection])
# cur = con.cursor()
#-------------------------------------------------------------------------------
# Executa os comando Delete no PostGreSQL
#-------------------------------------------------------------------------------
sql_delete =  """
------------------------------------------------------------
-- CICS_ABENDS_T;
------------------------------------------------------------
DELETE 
  FROM CICS_ABENDS_T
 WHERE MVS_SYSTEM_ID IN ('FIDY', 'FPR1')
   AND DATE >= DATE('$#@DATE@#$')
  WITH UR;
------------------------------------------------------------
"""
sql_delete = sql_delete.replace("$#@DATE@#$", sql_date)
#-------------------------------------------------------------------------------
# try:
#        cur.execute(sql_delete)
print("SQL Delete: ", sql_delete)
#-------------------------------------------------------------------------------
# Em caso de erro apresenta o comando SQL e mensagem de erro do PostGreSQL
# e cancela os Deletes no PostGreSQL
#-------------------------------------------------------------------------------
#except (Exception, psycopg2.DatabaseError) as error:
#    print("SQL Error, PostGreSQL:")
#    print("SQL Delete:", sql_delete)
#    print("SQL Error:", error)
#    con.rollback()
#-------------------------------------------------------------------------------
# Efetiva os Deletes no PostGreSQL
#-------------------------------------------------------------------------------
#finally:
#    if con is not None:
#        con.commit()
#-------------------------------------------------------------------------------
# Executa os comandos Inserts no PostGreSQL
#-------------------------------------------------------------------------------
sql_insert = ""
#-------------------------------------------------------------------------------
# try:
for sql_insert in sql_list:
#        cur.execute(sql_insert)
     print("SQL Insert: ", sql_insert)
#-------------------------------------------------------------------------------
# Em caso de erro apresenta o comando SQL e mensagem de erro do PostGreSQL
# e cancela os Inserts no PostGreSQL
#-------------------------------------------------------------------------------
#except (Exception, psycopg2.DatabaseError) as error:
#    print("SQL Error, PostGreSQL:")
#    print("SQL Insert:", sql_insert)
#    print("SQL Error:", error)
#    con.rollback()
#-------------------------------------------------------------------------------
# Efetiva os Inserts no PostGreSQL
#-------------------------------------------------------------------------------
#finally:
#    if con is not None:
#        con.commit()
#-------------------------------------------------------------------------------
# Fecha o Cursor e o Connection com o PostGreSQL
#-------------------------------------------------------------------------------
#cur.close()
#con.close()
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------