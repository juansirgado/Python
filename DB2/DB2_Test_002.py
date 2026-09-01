import ibm_db as db

conn = db.connect("DATABASE=DB2;HOSTNAME=127.0.0.1;PORT=25000;PROTOCOL=TCPIP;UID=db2admin;PWD=sirgadoa;", "", "")

for t in conn.tables():
    print(t)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Schema.Table")

for r in cursor.fetchall():
    print(r)
      
print("That is Folks!")