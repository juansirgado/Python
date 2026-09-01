#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import pyodbc     # pip install pyodbc # + IBM DB2 ODBC Driver #
import config     # file config.py
import system_log # file system_log.py
#-------------------------------------------------------------------------------
def db2_select(sql_select):
    #-------------------------------------------------------------------------------
    # print("DB2_Select: ", config.author)
    system_log.system_log("db2_select()", "Start")
    #-------------------------------------------------------------------------------
    # Cria o Connection e o Cursor com o DB2 via ODBC
    #-------------------------------------------------------------------------------
    # print("DB2 Connection: ", config.db2["connection"])
    con = pyodbc.connect(config.db2["connection"])
    cur = con.cursor()
    #-------------------------------------------------------------------------------
    # Executa o Select no DB2 e armazena os campos e os valores em formato Array
    #-------------------------------------------------------------------------------
    try:
        cur_status = cur.execute(sql_select)
        cur_desc = cur.description
        cur_vall = cur.fetchall()
    #-------------------------------------------------------------------------------
    # Em caso de erro apresenta o comando SQL e mensagem de erro do DB2
    #-------------------------------------------------------------------------------
    except (Exception, pyodbc.DatabaseError) as error:
        system_log.system_log("db2_select(Status)", cur_status)
        system_log.system_log("db2_select(Select)", sql_select)
        system_log.system_log("db2_select(Error)", error)
        # print("SQL Error, DB2:", cur_status)
        # print("SQL Select:", sql_select)
        # print("SQL Error:", error)
    #-------------------------------------------------------------------------------
    # Fecha o Cursor e o Connection com o DB2
    #-------------------------------------------------------------------------------
    cur.close()
    con.close()
    #-------------------------------------------------------------------------------
    system_log.system_log("db2_select()", "Stop")
    return(cur_desc, cur_vall)
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------