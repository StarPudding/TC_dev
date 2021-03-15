from django.db import models


if __name__ == '__main__':
    conn = pymysql.connect(
        'localhost',
        'root',
        'root',
        'test'
    )
    cursor = conn.cursor()

    cursor.execute("Select VERSION()")

    data = cursor.fetchone()

    print("Database version : %s" % data)

    conn.close()