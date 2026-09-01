#!/usr/bin/python
#-------------------------------------------------------------------------------
# Kyndryl Inc. Copyright © 2023. All rights reserved.
# By Juan Sirgado y Antico, 2023-12-10.
#-------------------------------------------------------------------------------
author = "Kyndryl Inc. Copyright © 2023. All rights reserved."
#-------------------------------------------------------------------------------
db2 = dict(
    type = "DB2",
    connection = "DSN=db9a;UID=a012327;PWD=cebola@3;",
    library = "pyodbc",
    driver = "odbc")
#-------------------------------------------------------------------------------
postgresql = dict(
    type = "PostGreSQL",
    connection = "host=192.168.1.14 port=5432 dbname=fisdbwl user=fisuser password=fispassword",
    library = "psycopg2",
    driver = "client")
#-------------------------------------------------------------------------------
# That is all Folks!
#-------------------------------------------------------------------------------