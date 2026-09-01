#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import psycopg2   # pip install psycopg2
import config     # file config.py
import system_log # file system_log.py
#-------------------------------------------------------------------------------
def postgresql_insert(sql_list):
    #-------------------------------------------------------------------------------
    # print("PostGreSQL_Insert: ", config.author)
    system_log.system_log("postgresql_insert()", "Start")
    #-------------------------------------------------------------------------------
    # Cria o Connection e o Cursor com o PostGreSQL
    #-------------------------------------------------------------------------------
    # print("PostGreSQL Connection: ", config.postgresql["connection"])
    con = psycopg2.connect(config.postgresql['connection'])
    cur = con.cursor()
    #-------------------------------------------------------------------------------
    # Executa os comandos Inserts no PostGreSQL
    #-------------------------------------------------------------------------------
    sql_insert = ""
    sql_count = len(sql_list)
    #-------------------------------------------------------------------------------
    try:
        for sql_index, sql_insert in enumerate(sql_list):
            cur_status = cur.execute(sql_insert)
            # if (sql_index <= 5):
            #    print("SQL Insert: ", sql_insert)
            # if (sql_index >= (sql_count - 5)):
            #    print("SQL Insert: ", sql_insert)

    #-------------------------------------------------------------------------------
    # Em caso de erro apresenta o comando SQL e mensagem de erro do PostGreSQL
    # e cancela os Inserts no PostGreSQL
    #-------------------------------------------------------------------------------
    except (Exception, psycopg2.DatabaseError) as error:
        system_log.system_log("postgresql_delete(Status)", cur_status)
        system_log.system_log("postgresql_delete(Select)", sql_insert)
        system_log.system_log("postgresql_delete(Error)", error)
        # print("SQL Error, PostGreSQL:", cur_status)
        # print("SQL Insert:", sql_insert)
        # print("SQL Error:", error)
        con.rollback()
    #-------------------------------------------------------------------------------
    # Efetiva os Inserts no PostGreSQL
    #-------------------------------------------------------------------------------
    finally:
        if (con is not None):
            con.commit()
    #-------------------------------------------------------------------------------
    # Fecha o Cursor e o Connection com o PostGreSQL
    #-------------------------------------------------------------------------------
    cur.close()
    con.close()
    #-------------------------------------------------------------------------------
    system_log.system_log("postgresql_insert()", "Stop")
    return (cur_status)
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------