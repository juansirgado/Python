import db2

conn = db2.connect(dsn='127.0.0.1', port='50000', uid='db2inst1', pwd='******')

curs = conn.cursor()
curs.execute('SELECT * FROM ORG')
rows = curs.fetchall()
rows