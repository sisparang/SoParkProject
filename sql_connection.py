import pymysql

conn = pymysql.connect(host='192.168.0.5', user='root', password='sisparang', db='sopark', charset='utf8')
curs = conn.cursor()

sql = "select * from sms"
sql2 = "insert into member (id, password, name) values (%s, %s, %s)"
curs.execute(sql2, ('test', '1234', 'tester'))

rows = curs.commit()

print(rows)

conn.close()

https://code.tutsplus.com/ko/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql-part-2--cms-22999