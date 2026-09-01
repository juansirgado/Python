import ibm_db_dbi as db

conn = db.connect("DATABASE=name;HOSTNAME=host;PORT=60000;PROTOCOL=TCPIP;UID=username;PWD=password;", "", "")

for t in conn.tables():
    print(t)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Schema.Table")

for r in cursor.fetchall():
    print(r)
      
print("That is Folks!")

================================================================================
import ibm_db
import sys


def get_connection():
    db_name = ""
    db_host_name = ""
    db_port = ""
    db_protocol = ""
    db_username = ""
    db_password = ""

    try:
        conn = ibm_db.connect(
        f"DATABASE = {db_name}; HOSTNAME = {db_host_name}; PORT = {db_port}; PROTOCOL = {db_protocol}; "
        f"UID = {db_username}; PWD = {db_password};", "", "")
        return conn
    except:
        print("no connection:", ibm_db.conn_errormsg())
        sys.exit(1)

get_connection()



================================================================================

import ibm_db
ibm_db.connect("DATABASE=name;HOSTNAME=host;PORT=60000;PROTOCOL=TCPIP;UID=username;
            PWD=password;", "", "")

================================================================================

query_str = "SELECT COUNT(*) FROM table_name"

conn = ibm_db.pconnect("dsn=write","usrname","secret")
query_stmt   = ibm_db.prepare(conn, query_str)
ibm_db.execute(query_stmt)


================================================================================

sql = " your insert/update/delete query here "
sql_command = {"commands":sql,"limit":1000,"separator":";","stop_on_error":"yes"}
service = "/sql_jobs"
r = requests.post(host+service,headers=auth_header,json=sql_command)
sql_command = {"commands":"COMMIT","limit":1000,"separator":";","stop_on_error":"yes"}
service = "/sql_jobs"
r = requests.post(host+service,headers=auth_header,json=sql_command)


================================================================================

sql = " your select query here "
service = "/sql_jobs"
r = requests.post(host+service,headers=auth_header,json=sql_command)
jobid = r.json()['id']
r = requests.get(host+service+"/"+jobid,headers=auth_header)
results = r.json()['results']
rows = results[0]['rows']

================================================================================



================================================================================




================================================================================




================================================================================
