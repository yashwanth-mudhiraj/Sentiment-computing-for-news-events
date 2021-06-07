import newspaper
import pymysql
import sentiment_mod as s

conn = pymysql.connect(host='localhost', user='root', password='', db='news',charset='utf8')

cursor = conn.cursor()

cnn_paper = newspaper.build('http://cnn.com/', memoize_articles=False)

for i in range(0,5):
    new_article = cnn_paper.articles[i]
    new_article.download()
    new_article.parse()
    try:
        cursor.execute("INSERT IGNORE INTO sentinews(TITLE,NEWS,IMAGE,SENTI,CODE) VALUES(%s,%s,%s,%s,%s)",
                       (new_article.title, new_article.text, new_article.top_image, 0, "a"))
        conn.commit()
    except Exception as e:
        print(e)


cursor.execute('SELECT * FROM sentinews')

result_set = []

for p in cursor.fetchall():
    result_set.append(s.sentiment(p[2]))

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

# print(newspaper.popular_urls())