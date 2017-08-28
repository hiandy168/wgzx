import pymysql
conn = pymysql.connect(host='172.25.252.243', port=3306, user='root', passwd='zabbix@mysql@243',db='dingding',charset='utf8')
cur = conn.cursor()
cur.execute('SELECT * FROM member')
for member in cur.fetchall():
   name,phone,num,group=member[1],member[2],member[3],member[4]
   print(name,phone,num,group)
cur.close()
conn.close()