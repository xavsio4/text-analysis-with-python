# this file will orchestrate all the others

# Write into mysql

def create_user(username, password):
    sql = ("INSERT INTO users(username, password) VALUES (%s, %s)")
    cursor.execute(sql, (username, password,))
    db.commit()
    user_id = cursor.lastrowid
    print("Added user {}".format(user_id))


def get_users():
    sql = ("SELECT * FROM users ORDER BY created DESC")
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        print(row)
