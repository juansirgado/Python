#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
import config             # file config.py
import db2_select         # file db2_select.py
import sql_insert         # file sql_insert.py
import postgresql_delete  # file postgresql_delete.py
import postgresql_insert  # file postgresql_insert.py
import system_log         # file system_log.py 
from datetime import date # pip install datetime
#-------------------------------------------------------------------------------
print("Author: ", config.author)
system_log.system_log("FIS_Workload()", "Start")
#-------------------------------------------------------------------------------
# Table e SQL usados para o Select e Insert com replace para a Data desejada
#-------------------------------------------------------------------------------
sql_date = str(date.today())
sql_table = "MVS_ADDRSUM_H"
sql_select =  """
------------------------------------------------------------
-- MVS_ADDRSUM_H;
------------------------------------------------------------
   SELECT VARCHAR_FORMAT(TIMESTAMP(T3.DATE, T3.TIME), 'YYYY-MM-DD HH24:MI:SS') AS DATETIME_TS
        , CHAR(T3.DATE, JIS) AS DATE_TS
        , CHAR(T3.TIME, JIS) AS TIME_TS
        , T3.MVS_SYSTEM_ID AS SYSTEM_ID
        , T3.TIPO_EMPRESA AS SERVICE_TYPE
        , SUM(T3.CPU_SEC) AS CPU_SEC
        , SUM(T3.MIPS) AS MIPS_SUM
   FROM (
      SELECT T1.DATE
           , T1.TIME
           , T1.MVS_SYSTEM_ID
           , CASE WHEN T1.TIPO_EMPRESA = 'BATCH'    THEN 'BATCH'
                  WHEN T1.TIPO_EMPRESA = 'ONLINE'   THEN 'ONLINE'
                  WHEN T1.TIPO_EMPRESA = 'STC'      THEN 'STC'
                  WHEN T1.TIPO_EMPRESA = 'REDE'     THEN 'NET'
                  WHEN T1.TIPO_EMPRESA = 'TSO'      THEN 'TSO'
                  WHEN T1.TIPO_EMPRESA = 'INFRA'    THEN 'INFRA'
                  WHEN T1.TIPO_EMPRESA = 'SIS-OPER' THEN 'SYSOP'
                  ELSE 'OTHERS'
                  END AS TIPO_EMPRESA
           , T1.CPU_TOTAL_SECONDS AS CPU_SEC
           , (T1.CPU_TOTAL_SECONDS * T2.MIPS_PER_SEC) AS MIPS
        FROM DRLFIS.MVS_ADDRSUM_H T1
           , DRLFIS.MVS_MIPS_HV1 T2
       WHERE T1.DATE >= DATE('$#@DATE@#$') - 2 DAYS
         AND T1.DATE <= DATE('$#@DATE@#$') - 1 DAY
         AND T1.MVS_SYSTEM_ID IN ('FIDY', 'FPR1', 'FIDD', 'FDEV', 'FIS0', 'FIS1')
         AND T1.CPU_TOTAL_SECONDS >= 0
         AND T1.DATE = T2.DATE
         AND T1.TIME = T2.TIME
         AND T1.MVS_SYSTEM_ID = T2.MVS_SYSTEM_ID
        ) T3
 GROUP BY T3.DATE
        , T3.TIME
        , T3.MVS_SYSTEM_ID
        , T3.TIPO_EMPRESA
 ORDER BY T3.DATE ASC
        , T3.TIME ASC
        , T3.MVS_SYSTEM_ID ASC
        , T3.TIPO_EMPRESA ASC
     WITH UR;
------------------------------------------------------------
"""
#-------------------------------------------------------------------------------
# Atualiza a Data na String SQL com a data corrente
#-------------------------------------------------------------------------------
sql_select = sql_select.replace("$#@DATE@#$", sql_date)
# print("SQL Select: ", sql_select)
#-------------------------------------------------------------------------------
# Executa o Select no DB2 e retorna os campos e os valores 
# em dois Arrays separados
#-------------------------------------------------------------------------------
cur_desc, cur_vall = db2_select.db2_select(sql_select)
# print("SQL Fields: ", cur_desc)
#-------------------------------------------------------------------------------
system_log.system_log("FIS_Workload()", "db2_select rows: " + str(len(cur_vall)))
#-------------------------------------------------------------------------------
# Com os valores retornados do Select monta os comandos Insert
# e retorna os comandos Insert agora com os valores em formato Array
#-------------------------------------------------------------------------------
sql_list = sql_insert.sql_insert(sql_table, cur_desc, cur_vall)
sql_rows = len(sql_list);
# print("SQL List Size: ", sql_rows)
# for sql_index in range(0,4,1) :
#     print("SQL Insert[", sql_index, ",0]: ", sql_list[sql_index])
# for sql_index in range(sql_rows-6, sql_rows-1,1):
#     print("SQL Insert[", sql_index, ",0]: ", sql_list[sql_index])
#-------------------------------------------------------------------------------
system_log.system_log("FIS_Workload()", "sql_insert rows: " + str(sql_rows))
#-------------------------------------------------------------------------------
# SQL usado para o Delete com replace para a Data desejada
#-------------------------------------------------------------------------------
sql_delete =  """
------------------------------------------------------------
-- MVS_ADDRSUM_H;
------------------------------------------------------------
DELETE
  FROM MVS_ADDRSUM_H
 WHERE SYSTEM_ID IN ('FIDY', 'FPR1', 'FIDD', 'FDEV', 'FIS0', 'FIS1')
   AND DATE_TS >= DATE('$#@DATE@#$') - INTERVAL '2 DAYS';
------------------------------------------------------------
"""
#-------------------------------------------------------------------------------
# Atualiza a Data na String SQL com a data corrente
#-------------------------------------------------------------------------------
sql_delete = sql_delete.replace("$#@DATE@#$", sql_date)
# print("SQL Delete: ", sql_delete)
#-------------------------------------------------------------------------------
# Executa o comando Delete no PostGreSQL dos dados parciais do ultimo periodo
# para evitar registros duplicados
#-------------------------------------------------------------------------------
sql_status = postgresql_delete.postgresql_delete(sql_delete)
# print("SQL Delete Status: ", sql_status)
#-------------------------------------------------------------------------------
# Executa os comandos Inserts no PostGreSQL com os dados atualizados 
# do periodo anterior e os novos dados para o periodo atual.
#-------------------------------------------------------------------------------
sql_status = postgresql_insert.postgresql_insert(sql_list)
# print("SQL Insert Status: ", sql_status)
#-------------------------------------------------------------------------------
system_log.system_log("FIS_Workload()", "Stop")
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------