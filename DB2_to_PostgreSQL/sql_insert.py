#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import config     # file config.py
import system_log # file system_log.py
#-------------------------------------------------------------------------------
def isfloat(num):
    #-------------------------------------------------------------------------------
    # Verifica se retorno do SQL é um valor float
    #-------------------------------------------------------------------------------
    try:
        float(num)
        return True
    except ValueError:
        return False
    #-------------------------------------------------------------------------------
def sql_insert(sql_table, cur_desc, cur_vall):
    #-------------------------------------------------------------------------------
    # print("SQL_Insert: ", config.author)
    system_log.system_log("sql_insert()", "Start")
    #-------------------------------------------------------------------------------
    # Cria o Prefix do SQL com o comando Insert e o nome dos campos sem os valores
    #-------------------------------------------------------------------------------
    sql_prefix = "INSERT INTO " + sql_table + " ("
    sql_sufix = ") VALUES ("
    sql_desc = ""
    col_last = len(cur_desc) - 1
    cur_len = len(cur_vall)
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
    for row_index, row_values in enumerate(cur_vall):
        sql_values = ""
        str_asp = ""
        for col_index, col_value in enumerate(row_values):
            str_value = str(col_value).strip()
            if (str_value.isnumeric() or isfloat(str_value)):
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
    system_log.system_log("sql_insert()", "Stop")
    return(sql_list)
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------