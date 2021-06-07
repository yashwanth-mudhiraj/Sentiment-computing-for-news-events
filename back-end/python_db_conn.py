import pymysql
import sentiment_mod as s

conn = pymysql.connect(host='localhost', user='root', password='', db='news')

cursor = conn.cursor()

cursor.execute('SELECT * FROM sentinews')

result_set = []

for p in cursor.fetchall():
    result_set.append(s.sentiment(p[2]))

print(result_set)

for i in list(range(len(result_set))):
    if result_set[i][0] == 'pos':
        try:
            cursor.execute("UPDATE sentinews SET CODE='pos',SENTI={} WHERE ID={}".format(result_set[i][1], i + 1))
            conn.commit()
        except Exception as e:
            print(e)

    elif result_set[i][0] == 'neg':
        try:
            cursor.execute("UPDATE sentinews SET CODE='neg',SENTI={} WHERE ID={}".format(result_set[i][1], i + 1))
            conn.commit()
        except Exception as e:
            print(e)

conn.autocommit(True)
conn.close()



